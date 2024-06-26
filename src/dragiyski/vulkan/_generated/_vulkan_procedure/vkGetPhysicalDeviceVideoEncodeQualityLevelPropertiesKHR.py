import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR import VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR
from .._vulkan_type.VkVideoEncodeQualityLevelPropertiesKHR import VkVideoEncodeQualityLevelPropertiesKHR

vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR), ctypes.POINTER(VkVideoEncodeQualityLevelPropertiesKHR))
