import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkLatencySleepInfoNV import VkLatencySleepInfoNV

vkLatencySleepNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkLatencySleepInfoNV))
