import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceProperties2 import VkPhysicalDeviceProperties2

vkGetPhysicalDeviceProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceProperties2))
