import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDebugReportCallbackCreateInfoEXT import VkDebugReportCallbackCreateInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDebugReportCallbackEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugReportCallbackCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
