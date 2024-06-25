import ctypes
from ..vulkan_base import VKAPI_PTR

from .._vulkan_type.VkDeviceMemoryReportCallbackDataEXT import VkDeviceMemoryReportCallbackDataEXT

vkDeviceMemoryReportCallbackEXT = VKAPI_PTR(None, ctypes.POINTER(VkDeviceMemoryReportCallbackDataEXT), ctypes.c_void_p)
