import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPerformanceOverrideInfoINTEL import VkPerformanceOverrideInfoINTEL

vkCmdSetPerformanceOverrideINTEL = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPerformanceOverrideInfoINTEL))
