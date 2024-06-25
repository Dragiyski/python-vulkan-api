import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkWriteDescriptorSet import VkWriteDescriptorSet
from .._vulkan_type.VkCopyDescriptorSet import VkCopyDescriptorSet

vkUpdateDescriptorSets = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet), ctypes.c_uint32, ctypes.POINTER(VkCopyDescriptorSet))
