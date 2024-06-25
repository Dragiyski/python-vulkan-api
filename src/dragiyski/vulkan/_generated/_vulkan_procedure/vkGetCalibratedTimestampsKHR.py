import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCalibratedTimestampInfoKHR import VkCalibratedTimestampInfoKHR

vkGetCalibratedTimestampsKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkCalibratedTimestampInfoKHR), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
