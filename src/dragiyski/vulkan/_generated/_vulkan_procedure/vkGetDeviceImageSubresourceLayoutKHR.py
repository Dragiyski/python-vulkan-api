import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceImageSubresourceInfoKHR import VkDeviceImageSubresourceInfoKHR
from .._vulkan_type.VkSubresourceLayout2KHR import VkSubresourceLayout2KHR

vkGetDeviceImageSubresourceLayoutKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageSubresourceInfoKHR), ctypes.POINTER(VkSubresourceLayout2KHR))
