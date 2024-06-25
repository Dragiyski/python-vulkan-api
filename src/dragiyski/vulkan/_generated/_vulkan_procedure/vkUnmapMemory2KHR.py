import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryUnmapInfoKHR import VkMemoryUnmapInfoKHR

vkUnmapMemory2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryUnmapInfoKHR))
