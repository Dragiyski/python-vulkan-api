import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkInstanceCreateInfo import VkInstanceCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateInstance = VKAPI_CALL(ctypes.c_int, ctypes.POINTER(VkInstanceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
