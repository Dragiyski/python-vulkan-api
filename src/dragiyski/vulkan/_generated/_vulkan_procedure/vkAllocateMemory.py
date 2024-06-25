import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryAllocateInfo import VkMemoryAllocateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkAllocateMemory = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryAllocateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
