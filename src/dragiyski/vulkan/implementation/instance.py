import ctypes

from collections.abc import Iterable
from weakref import finalize

from .. import binding
from ..version import VkVersion, VkApiVersion
from ..error import *

from .main import Loader as MainLoader, VkLayer, VkExtension, VkGlobal

class Loader:
    def __init__(self, instance: 'VkInstance', loader: MainLoader):
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
                ptr = ctypes.cast(self.loader.vkGetInstanceProcAddr(self.instance, c_name), ctypes.c_void_p).value
                if ptr is not None:
                    return signature(ptr)
        return object.__getattribute__(self, name)

class VkApplicationInfo:
    def __init__(
        self,
        api_version: VkApiVersion | VkVersion | int,
        application_name: str | bytes | None = None,
        application_version: VkApiVersion | VkVersion | int = 0,
        engine_name: str | bytes | None = None,
        engine_version: VkApiVersion | VkVersion | int = 0,
    ):
        self.api_version = api_version
        self.application_name = application_name
        self.application_version = application_version
        self.engine_name = engine_name
        self.engine_version = engine_version

        if isinstance(application_name, str):
            application_name = application_name.encode()
        if isinstance(engine_name, str):
            engine_name = engine_name.encode()
        
        self._as_parameter_ = binding.VkApplicationInfo(
            sType = binding.VK_STRUCTURE_TYPE_APPLICATION_INFO,
            pNext = None,
            pApplicationName = application_name,
            applicationVersion = application_version,
            pEngineName = engine_name,
            engineVersion = engine_version,
            apiVersion = api_version
        )

def _destroy_instance(vkDestroyInstance, *args):
    print('vkDestroyInstance(%s)' % ', '.join([repr(x) for x in args]))
    vkDestroyInstance(*args)

class VkInstance(binding.VkInstance):
    def __init__(
        self,
        context: VkGlobal,
        *,
        application_info: VkApplicationInfo,
        required_layers: Iterable[VkLayer | str | bytes] = [],
        optional_layers: Iterable[VkLayer | str | bytes] = [],
        required_extensions: Iterable[VkLayer | str | bytes] = [],
        optional_extensions: Iterable[VkLayer | str | bytes] = [],
        **kwargs
    ):
        super().__init__()
        required_layers = set(layer.encode() if isinstance(layer, str) else bytes(layer) for layer in required_layers)
        optional_layers = set(layer.encode() if isinstance(layer, str) else bytes(layer) for layer in optional_layers)
        required_extensions = set(extension.encode() if isinstance(extension, str) else bytes(extension) for extension in required_extensions)
        optional_extensions = set(extension.encode() if isinstance(extension, str) else bytes(extension) for extension in optional_extensions)
        if len(optional_layers) > 0:
            available_layers = set(layer.encode() for layer in vk_global.enumerate_instance_layer_properties())
            optional_layers = optional_layers.intersection(available_layers)
        layers = list(required_layers.union(optional_layers))
        if len(optional_extensions) > 0:
            available_extensions = set(extension.encode() for extension in vk_global.enumerate_instance_extension_properties())
            for layer in layers:
                available_extensions = available_extensions.union(set(extension.encode() for extension in vk_global.enumerate_instance_extension_properties(layer)))
            optional_extensions = optional_extensions.intersection(available_extensions)
        extensions = list(required_extensions.union(optional_extensions))

        # create_info_ext_list = []
        # for extension in extensions:
        #     if extension in self._ext_instance_create_info:
        #         struct = self._ext_instance_create_info(**kwargs)
        #         if struct is not None:
        #             create_info_ext_list.append(struct)
        
        # TODO: This should lookup into pNext of each extending structure, and locate the last pNext (where it is equal to None)
        # TODO: Only then we must assign pNext to the next structure, forming a single flat chain
        # TODO: The lines below will only work if every extensions create only a single extension structure.
        # for i in range(len(create_info_ext_list) - 1):
        #     create_info_ext_list[i].pNext = ctypes.pointer(create_info_ext_list[i + 1])

        ptr_layers = None
        ptr_extensions = None
        len_layers = len(layers)
        len_extensions = len(extensions)
        if len_layers > 0:
            array_layers = ctypes.c_char_p * len_layers
            for i in range(len_layers):
                array_layers[i] = layers[i]
            ptr_layers = ctypes.cast(array_layers, ctypes.POINTER(ctypes.c_char_p))
        if len_extensions > 0:
            array_extensions = ctypes.c_char_p * len_extensions
            for i in range(len_extensions):
                array_extensions[i] = extensions[i]
            ptr_extensions = ctypes.cast(array_extensions, ctypes.POINTER(ctypes.c_char_p))

        create_info = binding.VkInstanceCreateInfo(
            sType = binding.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
            pNext = None,
            pApplicationInfo = ctypes.pointer(application_info._as_parameter_),
            enabledLayerCount = len_layers,
            ppEnabledLayerNames = ptr_layers,
            enabledExtensionCount = len_extensions,
            ppEnabledExtensionNames = ptr_extensions
        )

        # TODO: Parameters for the allocation callbacks
        VkException.check(context._loader_.vkCreateInstance(ctypes.byref(create_info), None, ctypes.byref(self)))
        self._loader_ = Loader(self, context._loader_)
        self.__destroy = finalize(self, _destroy_instance, self._loader_.vkDestroyInstance, self.value, None)
    
    @property
    def alive(self):
        return self.__destroy.alive
    
    def destroy(self):
        self.__destroy()
