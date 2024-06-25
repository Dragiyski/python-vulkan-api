import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkClearAttachment import VkClearAttachment
from .._vulkan_type.VkClearRect import VkClearRect

vkCmdClearAttachments = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkClearAttachment), ctypes.c_uint32, ctypes.POINTER(VkClearRect))
