import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkValidationCacheCreateInfoEXT import VkValidationCacheCreateInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateValidationCacheEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkValidationCacheCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
