import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSemaphoreWaitInfo import VkSemaphoreWaitInfo

vkWaitSemaphores = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreWaitInfo), ctypes.c_uint64)
