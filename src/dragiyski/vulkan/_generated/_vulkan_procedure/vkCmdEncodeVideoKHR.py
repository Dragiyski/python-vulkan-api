import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoEncodeInfoKHR import VkVideoEncodeInfoKHR

vkCmdEncodeVideoKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkVideoEncodeInfoKHR))
