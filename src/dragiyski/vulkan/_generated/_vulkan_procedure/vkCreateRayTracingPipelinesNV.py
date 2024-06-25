import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRayTracingPipelineCreateInfoNV import VkRayTracingPipelineCreateInfoNV
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateRayTracingPipelinesNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
