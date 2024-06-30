import ctypes
from collections.abc import Iterable, Collection
from importlib import import_module

from .. import binding
from ..error import *
from ..loader import InstanceLoader
from .._pointer import finalize, PointerStorageType
from .._struct import pythonify_dict

import_module('.VkApplicationInfo', __package__)
import_module('.VkInstanceCreateInfo', __package__)


def _destroy_handle(vkDestroyInstance, *args):
    print('vkDestroyInstance(0x%016x)' % args[0])
    vkDestroyInstance(*args)

class VkInstance(metaclass = PointerStorageType):
    def __init__(self, application: 'Application', extensions: Iterable = (), layers: Iterable = ()):
        self._loader_ = InstanceLoader(application._loader_, self)
        self.application = application
        self.extensions = set(extensions)
        self.layers = set(layers)
        finalize(self._as_parameter_, self, _destroy_handle, self._loader_.vkDestroyInstance, self._as_parameter_, None)

    @classmethod
    def create(
        cls,
        application: 'Application',
        /, *,
        application_info: binding.VkApplicationInfo,
        layers: Iterable = (),
        extensions: Iterable = (),
        flags: binding.VkInstanceCreateFlags | int = 0
    ) -> 'VkInstance':
        create_info = binding.VkInstanceCreateInfo(
            flags = flags,
            application_info = application_info,
            layers = layers,
            extensions = extensions
        )

        handle = binding.VkInstance()
        VkException.check(application._loader_.vkCreateInstance(ctypes.byref(create_info), None, ctypes.byref(handle)))
        return cls(handle.value, application, extensions = extensions, layers = layers)

    def enumerate_physical_devices(self) -> 'Collection[VkPhysicalDevice]':
        vkEnumeratePhysicalDevices = self._loader_.vkEnumeratePhysicalDevices
        length = vkEnumeratePhysicalDevices.argtypes[1]._type_(0)
        try:
            VkException.check(vkEnumeratePhysicalDevices(self, ctypes.byref(length), None))
        except VkIncomplete:
            pass
        while True:
            c_array = (binding.VkPhysicalDevice * length.value)()
            try:
                VkException.check(
                    vkEnumeratePhysicalDevices(
                        self,
                        ctypes.byref(length),
                        ctypes.cast(c_array, vkEnumeratePhysicalDevices.argtypes[2])
                    )
                )
            except VkIncomplete:
                continue
            break
        return list(VkPhysicalDevice(handle, self) for handle in c_array)
    
    def enumerate_physical_device_groups(self):
        while True:
            try:
                vkEnumeratePhysicalDeviceGroups = self._loader_.vkEnumeratePhysicalDeviceGroups
                break
            except AttributeError:
                if 'VK_KHR_device_group_creation' in self.extensions:
                    try:
                        vkEnumeratePhysicalDeviceGroups = self._loader_.vkEnumeratePhysicalDeviceGroupsKHR
                        break
                    except AttributeError:
                        pass
            raise NotImplementedError('vkEnumeratePhysicalDeviceGroups')
        length = vkEnumeratePhysicalDeviceGroups.argtypes[1]._type_(0)
        try:
            VkException.check(vkEnumeratePhysicalDeviceGroups(self, ctypes.byref(length), None))
        except VkIncomplete:
            pass

        c_array = []
        def create_properties(properties: binding.VkPhysicalDeviceGroupProperties):
            return pythonify_dict({
                '__name__': properties.__class__.__name__,
                '_as_parameter_': properties,
                'devices': [VkPhysicalDevice(properties.physicalDevices[i], self) for i in range(properties.physicalDeviceCount)],
                'subset_allocation': properties.subsetAllocation
            })

        if length.value > 0:
            while True:
                c_array = (vkEnumeratePhysicalDeviceGroups.argtypes[2]._type_ * length.value)()
                try:
                    VkException.check(vkEnumeratePhysicalDeviceGroups(self, ctypes.byref(length), ctypes.cast(c_array, vkEnumeratePhysicalDeviceGroups.argtypes[2])))
                except VkIncomplete:
                    continue
                break

        return list(create_properties(c_array[i]) for i in range(length.value))


from .VkApplication import VkApplication
from .VkPhysicalDevice import VkPhysicalDevice
