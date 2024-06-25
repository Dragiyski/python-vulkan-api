import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageCopy import VkImageCopy

vkCmdCopyImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageCopy))
