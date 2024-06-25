import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageCreateInfo import VkImageCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateImage = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
