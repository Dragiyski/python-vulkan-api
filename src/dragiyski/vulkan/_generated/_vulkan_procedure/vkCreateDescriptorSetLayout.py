import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDescriptorSetLayoutCreateInfo import VkDescriptorSetLayoutCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDescriptorSetLayout = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetLayoutCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
