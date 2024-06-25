import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSamplerCreateInfo import VkSamplerCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateSampler = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
