import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetAccelerationStructureHandleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p)
