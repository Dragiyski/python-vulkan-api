import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSciSyncAttributesInfoNV import VkSciSyncAttributesInfoNV

vkGetPhysicalDeviceSciSyncAttributesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSciSyncAttributesInfoNV), ctypes.c_void_p)
