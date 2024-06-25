import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkExecutionGraphPipelineCreateInfoAMDX import VkExecutionGraphPipelineCreateInfoAMDX
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateExecutionGraphPipelinesAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkExecutionGraphPipelineCreateInfoAMDX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
