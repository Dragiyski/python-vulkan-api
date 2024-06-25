import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryWin32HandlePropertiesKHR import VkMemoryWin32HandlePropertiesKHR

vkGetMemoryWin32HandlePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkMemoryWin32HandlePropertiesKHR))
