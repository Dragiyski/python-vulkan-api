import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPipelineCacheCreateInfo import VkPipelineCacheCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreatePipelineCache = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineCacheCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
