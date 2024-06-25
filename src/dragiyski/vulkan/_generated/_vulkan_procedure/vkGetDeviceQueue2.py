import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceQueueInfo2 import VkDeviceQueueInfo2

vkGetDeviceQueue2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDeviceQueueInfo2), ctypes.POINTER(ctypes.c_void_p))
