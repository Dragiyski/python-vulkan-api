import ctypes
from ..vulkan_base import VKAPI_PTR

from .._vulkan_type.VkDebugUtilsMessengerCallbackDataEXT import VkDebugUtilsMessengerCallbackDataEXT

vkDebugUtilsMessengerCallbackEXT = VKAPI_PTR(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkDebugUtilsMessengerCallbackDataEXT), ctypes.c_void_p)
