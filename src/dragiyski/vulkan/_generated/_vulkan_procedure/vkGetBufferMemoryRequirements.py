import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryRequirements import VkMemoryRequirements

vkGetBufferMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkMemoryRequirements))
