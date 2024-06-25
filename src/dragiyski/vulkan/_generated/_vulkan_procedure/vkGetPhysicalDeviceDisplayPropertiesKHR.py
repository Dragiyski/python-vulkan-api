import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplayPropertiesKHR import VkDisplayPropertiesKHR

vkGetPhysicalDeviceDisplayPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayPropertiesKHR))
