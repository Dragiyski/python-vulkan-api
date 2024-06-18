import sys
from weakref import finalize
import ctypes

from typing import Iterable, Union

from .. import binding
from ..version import VkVersion, VkApiVersion
from ..error import *
from .._util import make_array_ptr_from_iterable


def _destroy_instance(vkDestroyInstance, handle):
    vkDestroyInstance(handle, None)

def _get_layer_name(layer):
    if isinstance(layer, binding.VkLayerProperties):
        layer = layer.layerName
    if isinstance(layer, str):
        layer = layer.encode()
    return ctypes.c_char_p(layer).value

def _get_extension_name(extension):
    if isinstance(extension, binding.VkExtensionProperties):
        extension = extension.layerName
    if isinstance(extension, str):
        extension = extension.encode()
    return ctypes.c_char_p(extension).value

class Instance:
    class _Loader:
        def __init__(self, instance, loader):
            self.instance = instance
            self.loader = loader

        def __getattr__(self, name):
            value = self.__getattr(name)
            object.__setattr__(self, name, value)
            return value

        def __getattr(self, name):
            c_name = name.encode()
            if name.startswith('vk') and hasattr(binding, name):
                signature = getattr(binding, name)
                if isinstance(signature, type) and issubclass(signature, ctypes._CFuncPtr):
                    ptr = ctypes.cast(self.loader.vkGetInstanceProcAddr(self.instance._Instance__handle, c_name), ctypes.c_void_p).value
                    if ptr is not None:
                        return signature(ptr)
            return object.__getattribute__(self, name)

    def __init__(
        self,
        library,
        loader,
        *,
        application_name: Union[str, bytes] = None,
        application_version: Union[int, VkVersion, VkApiVersion] = VkVersion(),
        engine_name: Union[str, bytes] = None,
        engine_version: Union[int, VkVersion, VkApiVersion] = VkVersion(),
        api_version: Union[int, VkVersion, VkApiVersion] = None,
        layers: Iterable[Union[str, bytes, binding.VkLayerProperties]] = [],
        extensions: Iterable[Union[str, bytes, binding.VkExtensionProperties]] = [],
        optional_extensions: Iterable[Union[str, bytes, binding.VkExtensionProperties]] = []
    ):
        if api_version is None:
            api_version = library.enumerate_instance_version()
        if isinstance(application_name, str):
            application_name = application_name.encode()
        if isinstance(engine_name, str):
            engine_name = engine_name.encode()
        layers = set(_get_layer_name(layer) for layer in layers)
        extensions = set(_get_extension_name(extension) for extension in extensions)
        optional_extensions = set(_get_extension_name(extension) for extension in optional_extensions)
        if len(optional_extensions) > 0:
            available_extensions = set(p.extensionName for p in library.enumerate_instance_extension_properties())
            for layer in layers:
                available_extensions = available_extensions.union(set(p.extensionName for p in library.enumerate_instance_extension_properties(layer)))
            extensions = extensions.union(optional_extensions.intersection(available_extensions))
        layer_count = len(layers)
        ptr_layers = make_array_ptr_from_iterable(ctypes.c_char_p, layers)
        ptr_extensions = make_array_ptr_from_iterable(ctypes.c_char_p, extensions)
        vk_application_info = binding.VkApplicationInfo(
            sType = binding.VK_STRUCTURE_TYPE_APPLICATION_INFO,
            pNext = None,
            pApplicationName = application_name,
            applicationVersion = int(application_version),
            pEngineName = engine_name,
            engineVersion = int(engine_version),
            apiVersion = int(api_version)
        )
        vk_create_instance_info = binding.VkInstanceCreateInfo(
            sType = binding.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
            pNext = None,
            flags = 0,
            pApplicationInfo = ctypes.pointer(vk_application_info),
            enabledLayerCount = len(layers),
            ppEnabledLayerNames = ptr_layers,
            enabledExtensionCount = len(extensions),
            ppEnabledExtensionNames = ptr_extensions
        )
        handle = loader.vkCreateInstance.argtypes[2]._type_()
        status_check(loader.vkCreateInstance(ctypes.byref(vk_create_instance_info), None, ctypes.byref(handle)))
        self.__handle = self._as_parameter_ = handle
        self.__loader = self._Loader(self, loader)
        self.__destroy = finalize(self, _destroy_instance, self.__loader.vkDestroyInstance, self.__handle)

    @property
    def alive(self):
        return self.__destroy.alive

    def destroy(self):
        self.__destroy()

    def create_debug_utils_messenger_EXT(
        self,
        **kwargs
    ):
        from . import DebugUtilsMessengerEXT
        return DebugUtilsMessengerEXT(self, self.__loader, **kwargs)


sys.modules[__name__] = Instance
