import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageSubresource2KHR import VkImageSubresource2KHR
from .._vulkan_type.VkSubresourceLayout2KHR import VkSubresourceLayout2KHR

vkGetImageSubresourceLayout2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageSubresource2KHR), ctypes.POINTER(VkSubresourceLayout2KHR))
