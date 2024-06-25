import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImportSemaphoreWin32HandleInfoKHR import VkImportSemaphoreWin32HandleInfoKHR

vkImportSemaphoreWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreWin32HandleInfoKHR))
