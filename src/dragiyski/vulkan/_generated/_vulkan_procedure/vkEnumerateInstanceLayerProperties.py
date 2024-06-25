import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkLayerProperties import VkLayerProperties

vkEnumerateInstanceLayerProperties = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkLayerProperties))
