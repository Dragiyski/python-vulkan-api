import ctypes
from ..vulkan_base import VKAPI_CALL


vkAcquireDrmDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int32, ctypes.c_void_p)
