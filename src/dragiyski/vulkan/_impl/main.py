import ctypes.util
from typing import Optional
from collections.abc import Callable

from .. import binding
from ..error import VkException, VkIncomplete
from .version import VkVersion, VkApiVersion

def get_vk_get_instance_proc_address(dlopen: 'Optional[Callable[[str], ctypes.CDLL|ctypes.WinDLL]]' = None) -> binding.vkGetInstanceProcAddr:
    name = ctypes.util.find_library('vulkan')
    if name is None:
        raise FileNotFoundError('Unable to locate the vulkan library')
    if dlopen is None:
        if hasattr(ctypes, 'WinDLL'):
            dlopen = ctypes.WinDLL
        else:
            dlopen = ctypes.CDLL
    lib = dlopen(name)
    ptr = lib.vkGetInstanceProcAddr
    return binding.vkGetInstanceProcAddr(ctypes.cast(ptr, ctypes.c_void_p).value)

class Loader:
    def __init__(self, vkGetInstanceProcAddr = None):
        if vkGetInstanceProcAddr is None:
            vkGetInstanceProcAddr = get_vk_get_instance_proc_address()
        if not callable(vkGetInstanceProcAddr):
            raise TypeError('vkGetInstanceProcAddr is not callable')
        self.vkGetInstanceProcAddr = vkGetInstanceProcAddr

    def __getattr__(self, name):
        value = self.__getattr(name)
        object.__setattr__(self, name, value)
        return value
    
    def __getattr(self, name):
        c_name = name.encode()
        if name.startswith('vk') and hasattr(binding, name):
            signature = getattr(binding, name)
            if isinstance(signature, type) and issubclass(signature, ctypes._CFuncPtr):
                ptr = ctypes.cast(self.vkGetInstanceProcAddr(None, c_name), ctypes.c_void_p).value
                if ptr is not None:
                    return signature(ptr)
        return object.__getattribute__(self, name)

class VkLayer(str):
    def __new__(cls, value: binding.VkLayerProperties):
        self = super().__new__(cls, value.layerName.decode())
        self.spec_version = VkApiVersion(value.specVersion)
        self.implementation_version = VkApiVersion(value.implementationVersion)
        self.description = value.description.decode()
        return self
    
class VkExtension(str):
    def __new__(cls, value: binding.VkExtensionProperties):
        self = super().__new__(cls, value.extensionName.decode())
        self.spec_version = VkApiVersion(value.specVersion)
        return self

class VkGlobal:
    def __init__(self, loader = Loader()):
        self._loader_ = loader

    def enumerate_instance_version(self, *, use_api_version = True):
        vkEnumerateInstanceVersion = self._loader_.vkEnumerateInstanceVersion
        c_version = vkEnumerateInstanceVersion.argtypes[0]._type_()
        VkException.check(vkEnumerateInstanceVersion(ctypes.byref(c_version)))
        return (VkApiVersion if use_api_version else VkVersion)(c_version.value)
    
    def enumerate_instance_layer_properties(self):
        vkEnumerateInstanceLayerProperties = self._loader_.vkEnumerateInstanceLayerProperties
        length = vkEnumerateInstanceLayerProperties.argtypes[0]._type_(0)
        try:
            VkException.check(vkEnumerateInstanceLayerProperties(ctypes.byref(length), None))
        except VkIncomplete:
            pass
        c_array = []
        while length.value > 0:
            c_array = (vkEnumerateInstanceLayerProperties.argtypes[1]._type_ * length.value)()
            c_ptr = ctypes.cast(c_array, vkEnumerateInstanceLayerProperties.argtypes[1])
            try:
                VkException.check(vkEnumerateInstanceLayerProperties(ctypes.byref(length), c_ptr))
            except VkIncomplete:
                continue
            break
        return list(VkLayer(c_array[i]) for i in range(length.value))
    

    
    def enumerate_instance_extension_properties(self, layer = None):
        if layer is not None:
            if isinstance(layer, str):
                layer = layer.encode()
        vkEnumerateInstanceExtensionProperties = self._loader_.vkEnumerateInstanceExtensionProperties
        length = vkEnumerateInstanceExtensionProperties.argtypes[1]._type_(0)
        try:
            VkException.check(vkEnumerateInstanceExtensionProperties(layer, ctypes.byref(length), None))
        except VkIncomplete:
            pass
        c_array = []
        while length.value > 0:
            c_array = (vkEnumerateInstanceExtensionProperties.argtypes[2]._type_ * length.value)()
            c_ptr = ctypes.cast(c_array, vkEnumerateInstanceExtensionProperties.argtypes[2])
            try:
                VkException.check(vkEnumerateInstanceExtensionProperties(layer, ctypes.byref(length), c_ptr))
            except VkIncomplete:
                continue
            break
        return list(VkExtension(c_array[i]) for i in range(length.value))
