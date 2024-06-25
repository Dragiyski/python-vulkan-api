import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetPrivateData = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
