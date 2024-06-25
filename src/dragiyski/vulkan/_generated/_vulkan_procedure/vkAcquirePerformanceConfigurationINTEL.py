import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPerformanceConfigurationAcquireInfoINTEL import VkPerformanceConfigurationAcquireInfoINTEL

vkAcquirePerformanceConfigurationINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceConfigurationAcquireInfoINTEL), ctypes.POINTER(ctypes.c_void_p))
