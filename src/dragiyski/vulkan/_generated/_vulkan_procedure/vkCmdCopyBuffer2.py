import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyBufferInfo2 import VkCopyBufferInfo2

vkCmdCopyBuffer2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyBufferInfo2))
