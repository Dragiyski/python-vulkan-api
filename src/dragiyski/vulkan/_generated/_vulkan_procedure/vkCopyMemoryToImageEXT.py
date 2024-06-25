import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyMemoryToImageInfoEXT import VkCopyMemoryToImageInfoEXT

vkCopyMemoryToImageEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToImageInfoEXT))
