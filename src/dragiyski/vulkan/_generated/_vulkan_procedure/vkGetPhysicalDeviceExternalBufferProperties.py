import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceExternalBufferInfo import VkPhysicalDeviceExternalBufferInfo
from .._vulkan_type.VkExternalBufferProperties import VkExternalBufferProperties

vkGetPhysicalDeviceExternalBufferProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalBufferInfo), ctypes.POINTER(VkExternalBufferProperties))
