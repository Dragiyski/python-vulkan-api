import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetPhysicalDeviceXcbPresentationSupportKHR = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32)
