import ctypes
from collections.abc import Iterable

from .. import binding
from ..error import *
from ..loader import InstanceLoader
from ..context import Context
from .._pointer import finalize, PointerStorageType


def _destroy_handle(vkDestroyInstance, *args):
    print('vkDestroyInstance(0x%016x)' % args[0])
    vkDestroyInstance(*args)


class VkInstance(metaclass = PointerStorageType):
    @classmethod
    def create(
        cls,
        application: 'Application',
        /, *,
        application_info: binding.VkApplicationInfo,
        required_layers: Iterable[str | bytes] = (),
        optional_layers: Iterable[str | bytes] = (),
        required_extensions: Iterable[str | bytes] = (),
        optional_extensions: Iterable[str | bytes] = (),
        flags: binding.VkInstanceCreateFlags | int = 0
    ):
        required_layers = set(layer.encode() if isinstance(layer, str) else bytes(layer) for layer in required_layers)
        optional_layers = set(layer.encode() if isinstance(layer, str) else bytes(layer) for layer in optional_layers)
        required_extensions = set(extension.encode() if isinstance(extension, str) else bytes(extension) for extension in required_extensions)
        optional_extensions = set(extension.encode() if isinstance(extension, str) else bytes(extension) for extension in optional_extensions)
        if len(optional_layers) > 0:
            available_layers = set(layer.encode() for layer in application.enumerate_instance_layer_properties())
            optional_layers = optional_layers.intersection(available_layers)
        layers = list(required_layers.union(optional_layers))
        if len(optional_extensions) > 0:
            available_extensions = set(extension.encode() for extension in application.enumerate_instance_extension_properties())
            for layer in layers:
                available_extensions = available_extensions.union(
                    set(extension.encode() for extension in application.enumerate_instance_extension_properties(layer))
                )
            optional_extensions = optional_extensions.intersection(available_extensions)
        extensions = list(required_extensions.union(optional_extensions))

        from .VkInstanceCreateInfo import VkInstanceCreateInfo

        create_info = VkInstanceCreateInfo.create(
            flags = flags,
            application_info = application_info,
            layers = layers,
            extensions = extensions
        )

        handle = binding.VkInstance()
        VkException.check(application._loader_.vkCreateInstance(ctypes.byref(create_info), None, ctypes.byref(handle)))
        self = object.__new__(cls)
        self._as_parameter_ = handle.value
        self._loader_ = InstanceLoader(application._loader_, self)
        finalize(handle.value, self, _destroy_handle, self._loader_.vkDestroyInstance, handle.value, None)
        return self

    def enumerate_physical_devices(self):
        vkEnumeratePhysicalDevices = self._loader_.vkEnumeratePhysicalDevices
        length = vkEnumeratePhysicalDevices.argtypes[1]._type_()
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
        from .VkPhysicalDevice import VkPhysicalDevice
        def initialize(ptr):
            obj = object.__new__(VkPhysicalDevice)
            obj._as_parameter_ = ptr
            obj._loader_ = self._loader_
            finalize(ptr, obj, None)
            return obj

        return list(initialize(value) for value in c_array)


from .Application import Application
