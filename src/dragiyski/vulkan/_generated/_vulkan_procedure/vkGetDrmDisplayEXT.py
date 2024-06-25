import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetDrmDisplayEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p))
