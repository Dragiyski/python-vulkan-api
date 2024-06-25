import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDescriptorUpdateTemplateCreateInfo import VkDescriptorUpdateTemplateCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDescriptorUpdateTemplate = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorUpdateTemplateCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
