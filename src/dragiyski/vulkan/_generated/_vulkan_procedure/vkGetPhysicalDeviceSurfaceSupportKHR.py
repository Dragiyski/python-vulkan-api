import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetPhysicalDeviceSurfaceSupportKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
