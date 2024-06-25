import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplayProperties2KHR import VkDisplayProperties2KHR

vkGetPhysicalDeviceDisplayProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayProperties2KHR))
