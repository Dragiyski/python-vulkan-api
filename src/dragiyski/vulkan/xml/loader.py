import ctypes
from abc import ABC, abstractmethod
from collections.abc import Callable

class Loader(ABC):
    __slots__ = ('binding', '__dict__')
    # def __getattr__(self, name: str):
    #     try:
    #         value = self._get_implementation(name)
    #     except NotImplementedError:
    #         raise AttributeError(name)
    #     self.__dict__[name] = value
    #     return value
    
    def __getitem__(self, name: str):
        if name in self.binding and name in self.__dict__:
            return self.__dict__[name]
        try:
            value = self._get_implementation(name)
        except NotImplementedError:
            raise KeyError(name)
        self.__dict__[name] = value
        return value
    
    def _get_implementation(self, name: str):
        try:
            binding = self.binding[name]
        except KeyError:
            raise NotImplementedError(f'Function {name} is not implemented')
        if isinstance(binding, type) and issubclass(binding, ctypes._CFuncPtr):
            ptr = self._get_function_address(name)
            if ptr is None:
                raise NotImplementedError(f'Function {name} is not implemented')
            return binding(ptr)
        return binding

    @abstractmethod
    def _get_function_address(self, name: str) -> int:
        pass

class LibraryLoader(Loader):
    __slots__ = ('binding', 'vkGetInstanceProcAddr')
    def __init__(self, binding, vkGetInstanceProcAddr: Callable|int):
        if isinstance(vkGetInstanceProcAddr, ctypes._CFuncPtr):
            vkGetInstanceProcAddr = ctypes.cast(vkGetInstanceProcAddr, ctypes.c_void_p).value
        if isinstance(vkGetInstanceProcAddr, int):
            vkGetInstanceProcAddr = binding['vkGetInstanceProcAddr'](vkGetInstanceProcAddr)
        self.binding = binding
        self.vkGetInstanceProcAddr = vkGetInstanceProcAddr
    
    def _get_function_address(self, name):
        return ctypes.cast(self.vkGetInstanceProcAddr(None, name.encode()), ctypes.c_void_p).value
    
class VkInstanceLoader(Loader):
    __slots__ = ('loader', 'instance')
    def __init__(self, loader: LibraryLoader, instance: int):
        self.loader = loader
        self.instance = instance
    
    def _get_function_address(self, name: str) -> int:
        return ctypes.cast(self.loader.vkGetInstanceProcAddr(self.instance, name.encode()), ctypes.c_void_p).value
    
    @property
    def binding(self):
        return self.loader.binding

class VkDeviceLoader(Loader):
    __slots__ = ('loader', 'device')
    def __init__(self, loader: LibraryLoader, device: int):
        self.loader = loader
        self.device = device
    
    def _get_function_address(self, name: str) -> int:
        return ctypes.cast(self.loader.vkGetDeviceProcAddr(self.device, name.encode()), ctypes.c_void_p).value
    
    @property
    def binding(self):
        return self.loader.binding
