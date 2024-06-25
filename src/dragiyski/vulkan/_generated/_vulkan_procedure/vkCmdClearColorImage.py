import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkClearColorValue import VkClearColorValue
from .._vulkan_type.VkImageSubresourceRange import VkImageSubresourceRange

vkCmdClearColorImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkClearColorValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
