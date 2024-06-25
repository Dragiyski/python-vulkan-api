import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSamplerYcbcrConversionCreateInfo import VkSamplerYcbcrConversionCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateSamplerYcbcrConversion = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerYcbcrConversionCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
