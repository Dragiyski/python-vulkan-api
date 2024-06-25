import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetDeviceMemoryCommitment = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64))
