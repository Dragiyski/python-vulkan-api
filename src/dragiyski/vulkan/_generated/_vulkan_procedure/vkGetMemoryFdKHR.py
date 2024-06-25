import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryGetFdInfoKHR import VkMemoryGetFdInfoKHR

vkGetMemoryFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
