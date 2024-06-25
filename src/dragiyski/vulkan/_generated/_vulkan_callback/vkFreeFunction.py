import ctypes
from ..vulkan_base import VKAPI_PTR


vkFreeFunction = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_void_p)
