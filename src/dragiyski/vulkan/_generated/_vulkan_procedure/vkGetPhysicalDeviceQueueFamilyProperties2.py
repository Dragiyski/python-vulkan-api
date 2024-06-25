import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkQueueFamilyProperties2 import VkQueueFamilyProperties2

vkGetPhysicalDeviceQueueFamilyProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties2))
