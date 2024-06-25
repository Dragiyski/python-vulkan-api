import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkQueueFamilyProperties import VkQueueFamilyProperties

vkGetPhysicalDeviceQueueFamilyProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkQueueFamilyProperties))
