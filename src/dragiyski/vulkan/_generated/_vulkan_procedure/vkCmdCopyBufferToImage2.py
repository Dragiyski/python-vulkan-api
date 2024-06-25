import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyBufferToImageInfo2 import VkCopyBufferToImageInfo2

vkCmdCopyBufferToImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyBufferToImageInfo2))
