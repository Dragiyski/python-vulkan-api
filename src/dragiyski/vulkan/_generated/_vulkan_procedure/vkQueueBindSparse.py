import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBindSparseInfo import VkBindSparseInfo

vkQueueBindSparse = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkBindSparseInfo), ctypes.c_void_p)
