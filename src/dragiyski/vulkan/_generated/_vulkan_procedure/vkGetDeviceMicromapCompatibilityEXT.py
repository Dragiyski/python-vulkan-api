import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMicromapVersionInfoEXT import VkMicromapVersionInfoEXT

vkGetDeviceMicromapCompatibilityEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkMicromapVersionInfoEXT), ctypes.POINTER(ctypes.c_int))
