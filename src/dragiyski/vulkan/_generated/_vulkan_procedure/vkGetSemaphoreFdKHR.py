import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSemaphoreGetFdInfoKHR import VkSemaphoreGetFdInfoKHR

vkGetSemaphoreFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
