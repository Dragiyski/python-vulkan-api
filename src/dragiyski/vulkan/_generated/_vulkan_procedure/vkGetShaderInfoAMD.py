import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetShaderInfoAMD = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(ctypes.c_size_t), ctypes.c_void_p)
