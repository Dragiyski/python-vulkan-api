import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceImageMemoryRequirements import VkDeviceImageMemoryRequirements
from .._vulkan_type.VkMemoryRequirements2 import VkMemoryRequirements2

vkGetDeviceImageMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageMemoryRequirements), ctypes.POINTER(VkMemoryRequirements2))
