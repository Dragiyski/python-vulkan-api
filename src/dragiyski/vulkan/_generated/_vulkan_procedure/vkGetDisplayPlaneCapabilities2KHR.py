import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplayPlaneInfo2KHR import VkDisplayPlaneInfo2KHR
from .._vulkan_type.VkDisplayPlaneCapabilities2KHR import VkDisplayPlaneCapabilities2KHR

vkGetDisplayPlaneCapabilities2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDisplayPlaneInfo2KHR), ctypes.POINTER(VkDisplayPlaneCapabilities2KHR))
