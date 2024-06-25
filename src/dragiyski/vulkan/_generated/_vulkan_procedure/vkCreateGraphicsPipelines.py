import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkGraphicsPipelineCreateInfo import VkGraphicsPipelineCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateGraphicsPipelines = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkGraphicsPipelineCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
