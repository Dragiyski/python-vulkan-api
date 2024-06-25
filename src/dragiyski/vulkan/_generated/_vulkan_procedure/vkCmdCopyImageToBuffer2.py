import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyImageToBufferInfo2 import VkCopyImageToBufferInfo2

vkCmdCopyImageToBuffer2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyImageToBufferInfo2))
