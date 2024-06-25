import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPerformanceValueINTEL import VkPerformanceValueINTEL

vkGetPerformanceParameterINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkPerformanceValueINTEL))
