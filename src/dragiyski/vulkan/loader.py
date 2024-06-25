import ctypes.util
from collections.abc import Callable
from . import binding


def locate_library():
    return ctypes.util.find_library('vulkan')


def load_library(loader_class = None):
    library = locate_library()
    if library is None:
        raise FileNotFoundError('Unable to locate library: %s' % 'vulkan')
    if loader_class is None:
        if hasattr(ctypes, 'WinDLL'):
            loader_class = ctypes.WinDLL
        else:
            loader_class = ctypes.CDLL
    return loader_class(library)


def get_vk_instance_get_proc_address(loader = load_library, *args, **kwargs):
    library = load_library(*args, **kwargs)
    return binding.vkGetInstanceProcAddr(ctypes.cast(library.vkGetInstanceProcAddr, ctypes.c_void_p).value)


class LibraryLoader:
    def __init__(self, vkGetInstanceProcAddr: Callable = get_vk_instance_get_proc_address()):
        if not callable(vkGetInstanceProcAddr):
            raise TypeError('Expected vkGetInstanceProcAddr to be a callable.')
        self.vkGetInstanceProcAddr = vkGetInstanceProcAddr

    def __getattr__(self, name):
        value = self.__getattr(name)
        object.__setattr__(self, name, value)
        return value

    def __getattr(self, name):
        c_name = name.encode()
        if hasattr(binding, name):
            signature = getattr(binding, name)
            if isinstance(signature, type) and issubclass(signature, ctypes._CFuncPtr):
                ptr = ctypes.cast(self.vkGetInstanceProcAddr(None, c_name), ctypes.c_void_p).value
                if ptr is not None:
                    return signature(ptr)
            else:
                return getattr(binding, name)
        raise AttributeError(name, name = name, obj = self)


class InstanceLoader:
    def __init__(self, loader: LibraryLoader, instance):
        self.loader = loader
        self.instance = instance

    def __getattr__(self, name):
        value = self.__getattr(name)
        object.__setattr__(self, name, value)
        return value

    def __getattr(self, name):
        c_name = name.encode()
        if hasattr(binding, name):
            signature = getattr(binding, name)
            if isinstance(signature, type) and issubclass(signature, ctypes._CFuncPtr):
                ptr = ctypes.cast(self.loader.vkGetInstanceProcAddr(self.instance, c_name), ctypes.c_void_p).value
                if ptr is not None:
                    return signature(ptr)
        raise AttributeError(name, name = name, obj = self)


class DeviceLoader:
    def __init__(self, loader: InstanceLoader, device: binding.VkDevice | int):
        self.loader = loader
        if isinstance(device, binding.VkDevice):
            device = device.value
        if not isinstance(device, int):
            raise TypeError('Argument "device" must be `int` or `VkDevice`.')
        self.device = device

    def __getattr__(self, name):
        value = self.__getattr(name)
        object.__setattr__(self, name, value)
        return value

    def __getattr(self, name):
        c_name = name.encode()
        if hasattr(binding, name):
            signature = getattr(binding, name)
            if isinstance(signature, type) and issubclass(signature, ctypes._CFuncPtr):
                ptr = ctypes.cast(self.loader.vkGetDeviceProcAddr(self.device, c_name), ctypes.c_void_p).value
                if ptr is not None:
                    return signature(ptr)
        raise AttributeError(name, name = name, obj = self)
