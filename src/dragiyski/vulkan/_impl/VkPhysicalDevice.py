import ctypes
from collections import namedtuple
from collections.abc import Collection

from .._pointer import finalize, PointerStorageType
from .. import binding
from ..version import *
from .._struct import build_out_struct_chain, pythonify_unchain_structure
from ..error import *
from .VkLayer import VkLayer
from .VkExtension import VkExtension

def _process_VkPhysicalDeviceProperties2(kv):
    properties = kv['properties']
    del kv['properties']
    kv.update(properties)
    return kv

def _process_VkQueueFamilyProperties2(kv):
    properties = kv['queue_family_properties']
    del kv['queue_family_properties']
    kv.update(properties)
    return kv

_get_properties_value_processor = {
    'VkPhysicalDeviceProperties': {
        'apiVersion': lambda value: VkApiVersion(value)
    }
}

_get_properties_dict_processor = {
    'VkPhysicalDeviceProperties2': _process_VkPhysicalDeviceProperties2
}

_get_family_queue_properties = {
    'VkQueueFamilyProperties2': _process_VkQueueFamilyProperties2
}

def _postprocess_dictionary(kv):
    for k, v in kv.items():
        if isinstance(v, dict) and '__name__' in v:
            kv[k] = _postprocess_dictionary(v)
    name = kv['__name__']
    del kv['__name__']
    return namedtuple(name, kv.keys())(*kv.values())

class VkPhysicalDevice(metaclass = PointerStorageType):
    def __init__(self, instance):
        self._loader_ = instance._loader_
        self.instance = instance
        finalize(self._as_parameter_, self, None)

    def _get_properties(self):
        vkGetPhysicalDeviceProperties = self._loader_.vkGetPhysicalDeviceProperties
        properties = binding.VkPhysicalDeviceProperties()
        vkGetPhysicalDeviceProperties(self, ctypes.byref(properties))
        return pythonify_unchain_structure(properties)
    
    def _get_properties_2(self):
        try:
            vkGetPhysicalDeviceProperties2 = self._loader_.vkGetPhysicalDeviceProperties2
        except AttributeError:
            raise NotImplementedError('vkGetPhysicalDeviceProperties2') from None

        vk_version = self._loader_.instance.application.enumerate_instance_version()
        properties = binding.VkPhysicalDeviceProperties2()
        build_out_struct_chain(properties, vk_version, self._loader_.instance.extensions)
        vkGetPhysicalDeviceProperties2(self, ctypes.byref(properties))
        return pythonify_unchain_structure(
            properties,
            dict_processor = _get_properties_dict_processor,
            value_processor = _get_properties_value_processor
        )

    def _get_properties_2_khr(self):
        try:
            vkGetPhysicalDeviceProperties2KHR = self._loader_.vkGetPhysicalDeviceProperties2KHR
        except AttributeError:
            raise NotImplementedError('vkGetPhysicalDeviceProperties2KHR') from None

        vk_version = self._loader_.instance.application.enumerate_instance_version()
        properties = binding.VkPhysicalDeviceProperties2()
        build_out_struct_chain(properties, vk_version, self._loader_.instance.extensions)
        vkGetPhysicalDeviceProperties2KHR(self, ctypes.byref(properties))
        return pythonify_unchain_structure(
            properties,
            dict_processor = _get_properties_dict_processor,
            value_processor = _get_properties_value_processor
        )

    def _get_family_queue_properties(self):
        vkGetPhysicalDeviceQueueFamilyProperties = self._loader_.vkGetPhysicalDeviceQueueFamilyProperties
        length = vkGetPhysicalDeviceQueueFamilyProperties.argtypes[1]._type_()
        vkGetPhysicalDeviceQueueFamilyProperties(self, ctypes.byref(length), None) # -> void
        c_array = []
        if length.value > 0:
            while True:
                last_value = length.value
                c_array = (vkGetPhysicalDeviceQueueFamilyProperties.argtypes[2]._type_ * length.value)()
                vkGetPhysicalDeviceQueueFamilyProperties(
                    self,
                    ctypes.byref(length),
                    ctypes.cast(c_array, vkGetPhysicalDeviceQueueFamilyProperties.argtypes[2])
                )
                if length.value > last_value:
                    continue
                break
        return list(pythonify_unchain_structure(c_array[i]) for i in range(length.value))

    def _get_family_queue_properties_2(self):
        try:
            vkGetPhysicalDeviceQueueFamilyProperties2 = self._loader_.vkGetPhysicalDeviceQueueFamilyProperties2
        except AttributeError:
            raise NotImplementedError('vkGetPhysicalDeviceProperties2KHR') from None
        
        length = vkGetPhysicalDeviceQueueFamilyProperties2.argtypes[1]._type_()
        vkGetPhysicalDeviceQueueFamilyProperties2(self, ctypes.byref(length), None) # -> void

        c_array = []
        if length.value > 0:
            vk_version = self._loader_.instance.application.enumerate_instance_version()
            while True:
                last_value = length.value
                c_array = (vkGetPhysicalDeviceQueueFamilyProperties2.argtypes[2]._type_ * length.value)()
                for i in range(length.value):
                    build_out_struct_chain(c_array[i], vk_version, self._loader_.instance.extensions)
                vkGetPhysicalDeviceQueueFamilyProperties2(
                    self,
                    ctypes.byref(length),
                    ctypes.cast(c_array, vkGetPhysicalDeviceQueueFamilyProperties2.argtypes[2])
                )
                if length.value > last_value:
                    continue
                break
        return list(pythonify_unchain_structure(c_array[i], dict_processor = _get_family_queue_properties) for i in range(length.value))

    def _get_family_queue_properties_2_khr(self):
        try:
            vkGetPhysicalDeviceQueueFamilyProperties2KHR = self._loader_.vkGetPhysicalDeviceQueueFamilyProperties2KHR
        except AttributeError:
            raise NotImplementedError('vkGetPhysicalDeviceProperties2KHR') from None
        
        length = vkGetPhysicalDeviceQueueFamilyProperties2KHR.argtypes[1]._type_()
        vkGetPhysicalDeviceQueueFamilyProperties2KHR(self, ctypes.byref(length), None) # -> void

        c_array = []
        if length.value > 0:
            vk_version = self._loader_.instance.application.enumerate_instance_version()
            while True:
                last_value = length.value
                c_array = (vkGetPhysicalDeviceQueueFamilyProperties2KHR.argtypes[2]._type_ * length.value)()
                for i in range(length.value):
                    build_out_struct_chain(c_array[i], vk_version, self._loader_.instance.extensions)
                vkGetPhysicalDeviceQueueFamilyProperties2KHR(
                    self,
                    ctypes.byref(length),
                    ctypes.cast(c_array, vkGetPhysicalDeviceQueueFamilyProperties2KHR.argtypes[2])
                )
                if length.value > last_value:
                    continue
                break
        return list(pythonify_unchain_structure(c_array[i], dict_processor = _get_family_queue_properties) for i in range(length.value))    

    def get_properties(self):
        fn_list = [self._get_properties_2, self._get_properties]
        if 'VK_KHR_get_physical_device_properties2' in self._loader_.instance.extensions:
            fn_list.insert(1, self._get_properties_2_khr)
        # Try this methods in order:
        # - vkGetPhysicalDeviceProperties2
        # - vkGetPhysicalDeviceProperties2KHR: only if VK_KHR_get_physical_device_properties2 is enabled
        # - vkGetPhysicalDeviceProperties
        for fn in fn_list:
            try:
                return fn()
            except NotImplementedError as error:
                continue
        raise error

    def get_family_queue_properties(self):
        fn_list = [self._get_family_queue_properties, self._get_family_queue_properties_2]
        if 'VK_KHR_get_physical_device_properties2' in self._loader_.instance.extensions:
            fn_list.insert(1, self._get_family_queue_properties_2_khr)
        # Try this methods in order:
        # - vkGetPhysicalDeviceQueueFamilyProperties2
        # - vkGetPhysicalDeviceQueueFamilyProperties2KHR: only if VK_KHR_get_physical_device_properties2 is enabled
        # - vkGetPhysicalDeviceQueueFamilyProperties
        for fn in fn_list:
            try:
                return fn()
            except NotImplementedError as error:
                continue
        raise error

    def enumerate_device_extension_properties(self) -> Collection[VkExtension]:
        if layer is not None:
            if isinstance(layer, str):
                layer = layer.encode()
        vkEnumerateDeviceExtensionProperties = self._loader_.vkEnumerateDeviceExtensionProperties
        length = vkEnumerateDeviceExtensionProperties.argtypes[2]._type_(0)
        try:
            VkException.check(vkEnumerateDeviceExtensionProperties(self, None, ctypes.byref(length), None))
        except VkIncomplete:
            pass
        c_array = []
        while length.value > 0:
            c_array = (vkEnumerateDeviceExtensionProperties.argtypes[3]._type_ * length.value)()
            c_ptr = ctypes.cast(c_array, vkEnumerateDeviceExtensionProperties.argtypes[3])
            try:
                VkException.check(vkEnumerateDeviceExtensionProperties(self, None, ctypes.byref(length), c_ptr))
            except VkIncomplete:
                continue
            break
        return list(VkExtension(c_array[i]) for i in range(length.value))
