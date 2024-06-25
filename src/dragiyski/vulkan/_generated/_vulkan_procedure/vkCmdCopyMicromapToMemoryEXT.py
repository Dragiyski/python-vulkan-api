import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyMicromapToMemoryInfoEXT import VkCopyMicromapToMemoryInfoEXT

vkCmdCopyMicromapToMemoryEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMicromapToMemoryInfoEXT))
