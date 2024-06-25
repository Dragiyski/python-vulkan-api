import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceSurfaceInfo2KHR import VkPhysicalDeviceSurfaceInfo2KHR
from .._vulkan_type.VkSurfaceFormat2KHR import VkSurfaceFormat2KHR

vkGetPhysicalDeviceSurfaceFormats2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSurfaceFormat2KHR))
