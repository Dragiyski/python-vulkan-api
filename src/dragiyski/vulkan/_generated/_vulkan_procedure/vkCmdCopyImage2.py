import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyImageInfo2 import VkCopyImageInfo2

vkCmdCopyImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyImageInfo2))
