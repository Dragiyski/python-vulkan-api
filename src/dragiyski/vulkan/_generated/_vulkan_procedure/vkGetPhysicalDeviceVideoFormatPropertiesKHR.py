import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceVideoFormatInfoKHR import VkPhysicalDeviceVideoFormatInfoKHR
from .._vulkan_type.VkVideoFormatPropertiesKHR import VkVideoFormatPropertiesKHR

vkGetPhysicalDeviceVideoFormatPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceVideoFormatInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkVideoFormatPropertiesKHR))
