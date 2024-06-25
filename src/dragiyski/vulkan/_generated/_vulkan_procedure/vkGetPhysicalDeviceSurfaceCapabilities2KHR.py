import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceSurfaceInfo2KHR import VkPhysicalDeviceSurfaceInfo2KHR
from .._vulkan_type.VkSurfaceCapabilities2KHR import VkSurfaceCapabilities2KHR

vkGetPhysicalDeviceSurfaceCapabilities2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(VkSurfaceCapabilities2KHR))
