import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceImageMemoryRequirements import VkDeviceImageMemoryRequirements
from .._vulkan_type.VkSparseImageMemoryRequirements2 import VkSparseImageMemoryRequirements2

vkGetDeviceImageSparseMemoryRequirements = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceImageMemoryRequirements), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageMemoryRequirements2))
