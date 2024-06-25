import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSwapchainCreateInfoKHR import VkSwapchainCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateSwapchainKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSwapchainCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
