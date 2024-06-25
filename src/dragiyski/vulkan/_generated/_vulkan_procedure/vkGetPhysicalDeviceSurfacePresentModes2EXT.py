import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceSurfaceInfo2KHR import VkPhysicalDeviceSurfaceInfo2KHR

vkGetPhysicalDeviceSurfacePresentModes2EXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSurfaceInfo2KHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_int))
