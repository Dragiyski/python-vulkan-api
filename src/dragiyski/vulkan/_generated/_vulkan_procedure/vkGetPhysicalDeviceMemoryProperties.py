import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceMemoryProperties import VkPhysicalDeviceMemoryProperties

vkGetPhysicalDeviceMemoryProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceMemoryProperties))
