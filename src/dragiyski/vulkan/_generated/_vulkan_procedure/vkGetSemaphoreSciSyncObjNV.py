import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSemaphoreGetSciSyncInfoNV import VkSemaphoreGetSciSyncInfoNV

vkGetSemaphoreSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetSciSyncInfoNV), ctypes.c_void_p)
