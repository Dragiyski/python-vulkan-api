import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDescriptorSetAllocateInfo import VkDescriptorSetAllocateInfo

vkAllocateDescriptorSets = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorSetAllocateInfo), ctypes.POINTER(ctypes.c_void_p))
