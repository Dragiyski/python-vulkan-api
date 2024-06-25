import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSparseImageFormatProperties import VkSparseImageFormatProperties

vkGetPhysicalDeviceSparseImageFormatProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkSparseImageFormatProperties))
