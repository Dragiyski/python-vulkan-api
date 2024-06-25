import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoEndCodingInfoKHR import VkVideoEndCodingInfoKHR

vkCmdEndVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoEndCodingInfoKHR))
