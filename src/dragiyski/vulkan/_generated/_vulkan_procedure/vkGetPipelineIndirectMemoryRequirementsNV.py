import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkComputePipelineCreateInfo import VkComputePipelineCreateInfo
from .._vulkan_type.VkMemoryRequirements2 import VkMemoryRequirements2

vkGetPipelineIndirectMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkComputePipelineCreateInfo), ctypes.POINTER(VkMemoryRequirements2))
