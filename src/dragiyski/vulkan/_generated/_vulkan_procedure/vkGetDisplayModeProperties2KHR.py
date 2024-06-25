import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplayModeProperties2KHR import VkDisplayModeProperties2KHR

vkGetDisplayModeProperties2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkDisplayModeProperties2KHR))
