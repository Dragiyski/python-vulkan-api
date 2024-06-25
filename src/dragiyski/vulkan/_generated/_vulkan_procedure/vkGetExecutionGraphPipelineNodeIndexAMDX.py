import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPipelineShaderStageNodeCreateInfoAMDX import VkPipelineShaderStageNodeCreateInfoAMDX

vkGetExecutionGraphPipelineNodeIndexAMDX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkPipelineShaderStageNodeCreateInfoAMDX), ctypes.POINTER(ctypes.c_uint32))
