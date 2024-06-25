import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSemaphoreGetWin32HandleInfoKHR import VkSemaphoreGetWin32HandleInfoKHR

vkGetSemaphoreWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
