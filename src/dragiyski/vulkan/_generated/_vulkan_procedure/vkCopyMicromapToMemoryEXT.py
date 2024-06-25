import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyMicromapToMemoryInfoEXT import VkCopyMicromapToMemoryInfoEXT

vkCopyMicromapToMemoryEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapToMemoryInfoEXT))
