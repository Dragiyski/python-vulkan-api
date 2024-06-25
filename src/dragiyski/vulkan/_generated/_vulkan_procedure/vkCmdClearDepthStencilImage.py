import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkClearDepthStencilValue import VkClearDepthStencilValue
from .._vulkan_type.VkImageSubresourceRange import VkImageSubresourceRange

vkCmdClearDepthStencilImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkClearDepthStencilValue), ctypes.c_uint32, ctypes.POINTER(VkImageSubresourceRange))
