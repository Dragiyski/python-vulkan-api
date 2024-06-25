import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplayPlanePropertiesKHR import VkDisplayPlanePropertiesKHR

vkGetPhysicalDeviceDisplayPlanePropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPlanePropertiesKHR))
