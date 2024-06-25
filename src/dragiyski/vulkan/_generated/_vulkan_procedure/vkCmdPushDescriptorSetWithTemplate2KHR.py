import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPushDescriptorSetWithTemplateInfoKHR import VkPushDescriptorSetWithTemplateInfoKHR

vkCmdPushDescriptorSetWithTemplate2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPushDescriptorSetWithTemplateInfoKHR))
