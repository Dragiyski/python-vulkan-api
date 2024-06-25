import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkExtensionProperties import VkExtensionProperties

vkEnumerateDeviceExtensionProperties = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkExtensionProperties))
