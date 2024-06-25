import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkQueryPoolPerformanceCreateInfoKHR import VkQueryPoolPerformanceCreateInfoKHR

vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkQueryPoolPerformanceCreateInfoKHR), ctypes.POINTER(ctypes.c_uint32))
