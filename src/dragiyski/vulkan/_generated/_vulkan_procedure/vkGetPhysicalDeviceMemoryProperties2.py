import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceMemoryProperties2 import VkPhysicalDeviceMemoryProperties2

vkGetPhysicalDeviceMemoryProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceMemoryProperties2))
