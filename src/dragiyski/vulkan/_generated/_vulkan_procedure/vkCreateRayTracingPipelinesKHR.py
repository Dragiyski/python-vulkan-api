import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRayTracingPipelineCreateInfoKHR import VkRayTracingPipelineCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateRayTracingPipelinesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRayTracingPipelineCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
