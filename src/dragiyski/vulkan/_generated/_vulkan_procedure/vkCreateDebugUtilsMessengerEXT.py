import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDebugUtilsMessengerCreateInfoEXT import VkDebugUtilsMessengerCreateInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDebugUtilsMessengerEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugUtilsMessengerCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
