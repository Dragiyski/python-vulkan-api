import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkFenceGetWin32HandleInfoKHR import VkFenceGetWin32HandleInfoKHR

vkGetFenceWin32HandleKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetWin32HandleInfoKHR), ctypes.POINTER(ctypes.c_void_p))
