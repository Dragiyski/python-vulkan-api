import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkGeneratedCommandsMemoryRequirementsInfoNV import VkGeneratedCommandsMemoryRequirementsInfoNV
from .._vulkan_type.VkMemoryRequirements2 import VkMemoryRequirements2

vkGetGeneratedCommandsMemoryRequirementsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkGeneratedCommandsMemoryRequirementsInfoNV), ctypes.POINTER(VkMemoryRequirements2))
