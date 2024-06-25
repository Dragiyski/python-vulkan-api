import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPipelineExecutableInfoKHR import VkPipelineExecutableInfoKHR
from .._vulkan_type.VkPipelineExecutableStatisticKHR import VkPipelineExecutableStatisticKHR

vkGetPipelineExecutableStatisticsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableStatisticKHR))
