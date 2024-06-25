import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceFeatures import VkPhysicalDeviceFeatures

vkGetPhysicalDeviceFeatures = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceFeatures))
