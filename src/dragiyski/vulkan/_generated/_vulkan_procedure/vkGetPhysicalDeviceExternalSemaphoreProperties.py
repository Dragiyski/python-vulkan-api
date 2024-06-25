import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPhysicalDeviceExternalSemaphoreInfo import VkPhysicalDeviceExternalSemaphoreInfo
from .._vulkan_type.VkExternalSemaphoreProperties import VkExternalSemaphoreProperties

vkGetPhysicalDeviceExternalSemaphoreProperties = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkPhysicalDeviceExternalSemaphoreInfo), ctypes.POINTER(VkExternalSemaphoreProperties))
