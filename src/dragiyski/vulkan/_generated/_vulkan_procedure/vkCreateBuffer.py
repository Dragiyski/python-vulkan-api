import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBufferCreateInfo import VkBufferCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateBuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
