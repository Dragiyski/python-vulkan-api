import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkFormatProperties import VkFormatProperties

vkGetPhysicalDeviceFormatProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkFormatProperties))
