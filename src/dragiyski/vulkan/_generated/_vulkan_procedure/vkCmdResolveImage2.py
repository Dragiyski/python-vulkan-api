import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkResolveImageInfo2 import VkResolveImageInfo2

vkCmdResolveImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkResolveImageInfo2))
