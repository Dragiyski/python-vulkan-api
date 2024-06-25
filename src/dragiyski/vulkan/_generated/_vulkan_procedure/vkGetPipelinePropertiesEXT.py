import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPipelineInfoKHR import VkPipelineInfoKHR
from .._vulkan_type.VkBaseOutStructure import VkBaseOutStructure

vkGetPipelinePropertiesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineInfoKHR), ctypes.POINTER(VkBaseOutStructure))
