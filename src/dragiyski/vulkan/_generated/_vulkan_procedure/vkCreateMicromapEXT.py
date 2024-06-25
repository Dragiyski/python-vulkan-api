import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMicromapCreateInfoEXT import VkMicromapCreateInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateMicromapEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMicromapCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
