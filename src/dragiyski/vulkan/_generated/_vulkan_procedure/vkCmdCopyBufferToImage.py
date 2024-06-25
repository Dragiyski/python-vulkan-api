import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBufferImageCopy import VkBufferImageCopy

vkCmdCopyBufferToImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkBufferImageCopy))
