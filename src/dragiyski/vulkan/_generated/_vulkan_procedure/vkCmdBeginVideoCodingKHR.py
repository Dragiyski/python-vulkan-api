import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoBeginCodingInfoKHR import VkVideoBeginCodingInfoKHR

vkCmdBeginVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoBeginCodingInfoKHR))
