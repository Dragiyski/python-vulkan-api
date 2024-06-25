import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSemaphoreSciSyncPoolCreateInfoNV import VkSemaphoreSciSyncPoolCreateInfoNV
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateSemaphoreSciSyncPoolNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreSciSyncPoolCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
