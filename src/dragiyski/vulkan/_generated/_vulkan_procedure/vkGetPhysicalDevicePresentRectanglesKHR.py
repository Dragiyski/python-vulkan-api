import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRect2D import VkRect2D

vkGetPhysicalDevicePresentRectanglesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkRect2D))
