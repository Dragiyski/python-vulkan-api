import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRefreshCycleDurationGOOGLE import VkRefreshCycleDurationGOOGLE

vkGetRefreshCycleDurationGOOGLE = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkRefreshCycleDurationGOOGLE))
