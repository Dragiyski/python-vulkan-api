import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPushConstantsInfoKHR import VkPushConstantsInfoKHR

vkCmdPushConstants2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushConstantsInfoKHR))
