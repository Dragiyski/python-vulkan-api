import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkFenceGetSciSyncInfoNV import VkFenceGetSciSyncInfoNV

vkGetFenceSciSyncObjNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetSciSyncInfoNV), ctypes.c_void_p)
