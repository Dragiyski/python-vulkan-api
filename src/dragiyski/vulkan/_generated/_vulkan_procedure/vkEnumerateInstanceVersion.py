import ctypes
from ..vulkan_base import VKAPI_CALL


vkEnumerateInstanceVersion = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(ctypes.c_uint32))
