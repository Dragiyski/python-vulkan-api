import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPushDescriptorSetInfoKHR import VkPushDescriptorSetInfoKHR

vkCmdPushDescriptorSet2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushDescriptorSetInfoKHR))
