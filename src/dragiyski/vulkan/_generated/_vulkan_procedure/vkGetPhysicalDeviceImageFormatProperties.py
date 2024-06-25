import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageFormatProperties import VkImageFormatProperties

vkGetPhysicalDeviceImageFormatProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkImageFormatProperties))
