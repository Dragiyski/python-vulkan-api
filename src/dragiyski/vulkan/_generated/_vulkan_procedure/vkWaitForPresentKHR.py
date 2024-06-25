import ctypes
from ..vulkan_base import VKAPI_CALL


vkWaitForPresentKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint64)
