import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceSparseImageFormatInfo2 import VkPhysicalDeviceSparseImageFormatInfo2
from .._vulkan_type.VkSparseImageFormatProperties2 import VkSparseImageFormatProperties2

vkGetPhysicalDeviceSparseImageFormatProperties2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceSparseImageFormatInfo2), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties2))
