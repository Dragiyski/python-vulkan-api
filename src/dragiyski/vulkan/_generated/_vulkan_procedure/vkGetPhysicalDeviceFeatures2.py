import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceFeatures2 import VkPhysicalDeviceFeatures2

vkGetPhysicalDeviceFeatures2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceFeatures2))
