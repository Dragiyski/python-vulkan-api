import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkFormatProperties2 import VkFormatProperties2

vkGetPhysicalDeviceFormatProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkFormatProperties2))
