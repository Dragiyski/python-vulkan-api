import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAcquireNextImageInfoKHR import VkAcquireNextImageInfoKHR

vkAcquireNextImage2KHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAcquireNextImageInfoKHR), ctypes.POINTER(ctypes.c_uint32))
