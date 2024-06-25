import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkInitializePerformanceApiInfoINTEL import VkInitializePerformanceApiInfoINTEL

vkInitializePerformanceApiINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkInitializePerformanceApiInfoINTEL))
