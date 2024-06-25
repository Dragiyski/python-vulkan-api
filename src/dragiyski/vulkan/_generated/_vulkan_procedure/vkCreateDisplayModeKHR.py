import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplayModeCreateInfoKHR import VkDisplayModeCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDisplayModeKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayModeCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
