import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageSparseMemoryRequirementsInfo2 import VkImageSparseMemoryRequirementsInfo2
from .._vulkan_type.VkSparseImageMemoryRequirements2 import VkSparseImageMemoryRequirements2

vkGetImageSparseMemoryRequirements2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkImageSparseMemoryRequirementsInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2))
