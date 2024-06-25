import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCheckpointDataNV import VkCheckpointDataNV

vkGetQueueCheckpointDataNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkCheckpointDataNV))
