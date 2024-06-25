import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImportFenceWin32HandleInfoKHR import VkImportFenceWin32HandleInfoKHR

vkImportFenceWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportFenceWin32HandleInfoKHR))
