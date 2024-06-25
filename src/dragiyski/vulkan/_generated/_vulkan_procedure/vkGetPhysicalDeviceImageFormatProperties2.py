import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceImageFormatInfo2 import VkPhysicalDeviceImageFormatInfo2
from .._vulkan_type.VkImageFormatProperties2 import VkImageFormatProperties2

vkGetPhysicalDeviceImageFormatProperties2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceImageFormatInfo2), ctypes.POINTER(VkImageFormatProperties2))
