import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDescriptorPoolCreateInfo import VkDescriptorPoolCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDescriptorPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDescriptorPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
