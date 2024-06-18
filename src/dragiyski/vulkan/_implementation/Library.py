import ctypes.util
import sys

from typing import Union, Iterable

from .. import binding
from ..version import VkVersion, VkApiVersion
from ..error import *


class Library:
    class NotFoundError(Exception):
        pass

    class __Loader:
        def __init__(self, vkGetInstanceProcAddr):
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

    def __init__(self):
        self.__loader = self.__Loader(self._load_get_instance_proc_address())

    def _load_get_instance_proc_address(self):
        name = ctypes.util.find_library('vulkan')
        if name is None:
            raise Library.NotFoundError('Unable to find vulkan library')
        if hasattr(ctypes, 'WinDLL'):
            lib = ctypes.WinDLL(name)
        else:
            lib = ctypes.CDLL(name)
        ptr_get_instance_proc_addr = lib.vkGetInstanceProcAddr
        return binding.vkGetInstanceProcAddr(ctypes.cast(ptr_get_instance_proc_addr, ctypes.c_void_p).value)

    def enumerate_instance_version(self, use_api = False):
        version = (VkApiVersion if use_api else VkVersion)()
        status_check(self.__loader.vkEnumerateInstanceVersion(version))
        return version

    def enumerate_instance_layer_properties(self):
        vkEnumerateInstanceLayerProperties = self.__loader.vkEnumerateInstanceLayerProperties
        count = vkEnumerateInstanceLayerProperties.argtypes[0]._type_(0)
        try:
            status_check(vkEnumerateInstanceLayerProperties(ctypes.byref(count), None))
        except VkIncomplete:
            pass
        c_array = []
        while count.value > 0:
            c_array = ctypes.ARRAY(vkEnumerateInstanceLayerProperties.argtypes[1]._type_, count.value)()
            try:
                status_check(vkEnumerateInstanceLayerProperties(ctypes.byref(count), ctypes.cast(c_array, vkEnumerateInstanceLayerProperties.argtypes[1])))
            except VkIncomplete:
                continue
            break
        return list(c_array[i] for i in range(count.value))

    def enumerate_instance_extension_properties(self, layer = None):
        if layer is not None:
            if isinstance(layer, str):
                layer = layer.encode()
            layer = ctypes.c_char_p(layer)
        vkEnumerateInstanceExtensionProperties = self.__loader.vkEnumerateInstanceExtensionProperties
        count = vkEnumerateInstanceExtensionProperties.argtypes[1]._type_(0)
        try:
            status_check(vkEnumerateInstanceExtensionProperties(layer, ctypes.byref(count), None))
        except VkIncomplete:
            pass
        c_array = []
        while count.value > 0:
            c_array = ctypes.ARRAY(vkEnumerateInstanceExtensionProperties.argtypes[2]._type_, count.value)()
            try:
                status_check(
                    vkEnumerateInstanceExtensionProperties(
                        layer,
                        ctypes.byref(count),
                        ctypes.cast(c_array, vkEnumerateInstanceExtensionProperties.argtypes[2])
                    )
                )
            except VkIncomplete:
                continue
            break
        return list(c_array[i] for i in range(count.value))

    def create_instance(
        self,
        **kwargs,
    ):
        from . import Instance
        return Instance(self, self.__loader, **kwargs)


sys.modules[__name__] = Library
