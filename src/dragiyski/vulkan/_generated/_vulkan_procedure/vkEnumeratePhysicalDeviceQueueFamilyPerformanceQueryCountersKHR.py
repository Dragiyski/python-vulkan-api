import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPerformanceCounterKHR import VkPerformanceCounterKHR
from .._vulkan_type.VkPerformanceCounterDescriptionKHR import VkPerformanceCounterDescriptionKHR

vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPerformanceCounterKHR), ctypes.POINTER(VkPerformanceCounterDescriptionKHR))
