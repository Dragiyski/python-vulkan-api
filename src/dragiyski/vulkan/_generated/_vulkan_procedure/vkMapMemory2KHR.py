import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryMapInfoKHR import VkMemoryMapInfoKHR

vkMapMemory2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryMapInfoKHR), ctypes.POINTER(ctypes.c_void_p))
