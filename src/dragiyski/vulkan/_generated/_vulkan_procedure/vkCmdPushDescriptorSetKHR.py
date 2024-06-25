import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkWriteDescriptorSet import VkWriteDescriptorSet

vkCmdPushDescriptorSetKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkWriteDescriptorSet))
