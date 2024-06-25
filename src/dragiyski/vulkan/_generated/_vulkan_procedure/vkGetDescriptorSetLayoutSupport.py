import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDescriptorSetLayoutCreateInfo import VkDescriptorSetLayoutCreateInfo
from .._vulkan_type.VkDescriptorSetLayoutSupport import VkDescriptorSetLayoutSupport

vkGetDescriptorSetLayoutSupport = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkDescriptorSetLayoutSupport))
