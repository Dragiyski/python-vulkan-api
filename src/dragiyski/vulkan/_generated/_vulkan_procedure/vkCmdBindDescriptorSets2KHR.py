import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBindDescriptorSetsInfoKHR import VkBindDescriptorSetsInfoKHR

vkCmdBindDescriptorSets2KHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBindDescriptorSetsInfoKHR))
