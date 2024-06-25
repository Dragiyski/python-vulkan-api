import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkQueryPoolCreateInfo import VkQueryPoolCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateQueryPool = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkQueryPoolCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
