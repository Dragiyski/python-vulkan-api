import ctypes
from . import _vulkan_binding

class Library:
    def __init__(self, *args, **kwargs):
        self._load(*args, **kwargs)

    def _load(self, *args, **kwargs):
        import ctypes.util
        name = ctypes.util.find_library('vulkan')
        if name is None:
            raise RuntimeError('Unable to find a vulkan library.')
        if hasattr(ctypes, 'WinDLL'):
            # On Windows, the default API calls are stdcall.
            self.__handle = ctypes.WinDLL(name)
        else:
            # On all other (Unix-based) platforms: cdecl
            self.__handle = ctypes.CDLL(name)
        self.__vkGetInstanceProcAddress = _vulkan_binding.vkGetInstanceProcAddr(self.__handle.vkGetInstanceProcAddr)

    def _import_function(self, signature, name: str):
        try:
            ptr = getattr(self.__handle, name)
        except AttributeError as error:
            raise AttributeError('No function named %s found in the vulkan library.' % name, name = name, obj = self) from error
        return signature(ptr)

    def __getattr__(self, name):
        value = self.__getattr(name)
        object.__setattr__(self, name, value)
        return value

    def __getattr(self, name):
        if name.startswith('_') or not hasattr(_vulkan_binding, name):
            return object.__getattr__(self, name)
        value = getattr(_vulkan_binding, name)
        if isinstance(value, type) and issubclass(value, ctypes._CFuncPtr):
            value = self._import_function(value, name)
        return value

    def __dir__(self):
        return set(name for name in dir(_vulkan_binding) if not name.startswith('_')).union(object.__dir__(self))