import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBufferMemoryRequirementsInfo2 import VkBufferMemoryRequirementsInfo2
from .._vulkan_type.VkMemoryRequirements2 import VkMemoryRequirements2

vkGetBufferMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBufferMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
