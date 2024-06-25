import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageMemoryRequirementsInfo2 import VkImageMemoryRequirementsInfo2
from .._vulkan_type.VkMemoryRequirements2 import VkMemoryRequirements2

vkGetImageMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkImageMemoryRequirementsInfo2), ctypes.POINTER(VkMemoryRequirements2))
