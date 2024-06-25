import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoCodingControlInfoKHR import VkVideoCodingControlInfoKHR

vkCmdControlVideoCodingKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoCodingControlInfoKHR))
