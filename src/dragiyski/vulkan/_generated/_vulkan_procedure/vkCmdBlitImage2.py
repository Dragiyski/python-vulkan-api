import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBlitImageInfo2 import VkBlitImageInfo2

vkCmdBlitImage2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBlitImageInfo2))
