import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBufferViewCreateInfo import VkBufferViewCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateBufferView = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferViewCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
