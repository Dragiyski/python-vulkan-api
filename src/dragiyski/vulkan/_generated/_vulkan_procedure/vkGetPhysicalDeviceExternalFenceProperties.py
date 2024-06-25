import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceExternalFenceInfo import VkPhysicalDeviceExternalFenceInfo
from .._vulkan_type.VkExternalFenceProperties import VkExternalFenceProperties

vkGetPhysicalDeviceExternalFenceProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalFenceInfo), ctypes.POINTER(VkExternalFenceProperties))
