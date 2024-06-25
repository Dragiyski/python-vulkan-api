import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBindBufferMemoryInfo import VkBindBufferMemoryInfo

vkBindBufferMemory2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindBufferMemoryInfo))
