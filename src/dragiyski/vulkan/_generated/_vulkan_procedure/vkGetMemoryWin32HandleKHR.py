import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryGetWin32HandleInfoKHR import VkMemoryGetWin32HandleInfoKHR

vkGetMemoryWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
