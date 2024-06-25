import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPipelineExecutableInfoKHR import VkPipelineExecutableInfoKHR
from .._vulkan_type.VkPipelineExecutableInternalRepresentationKHR import VkPipelineExecutableInternalRepresentationKHR

vkGetPipelineExecutableInternalRepresentationsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPipelineExecutableInfoKHR), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(VkPipelineExecutableInternalRepresentationKHR))
