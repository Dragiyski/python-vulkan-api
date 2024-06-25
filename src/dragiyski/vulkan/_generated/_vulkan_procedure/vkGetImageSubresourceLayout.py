import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageSubresource import VkImageSubresource
from .._vulkan_type.VkSubresourceLayout import VkSubresourceLayout

vkGetImageSubresourceLayout = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkImageSubresource), ctypes.POINTER(VkSubresourceLayout))
