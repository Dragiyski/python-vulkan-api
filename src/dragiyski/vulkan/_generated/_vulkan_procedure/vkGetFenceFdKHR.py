import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkFenceGetFdInfoKHR import VkFenceGetFdInfoKHR

vkGetFenceFdKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceGetFdInfoKHR), ctypes.POINTER(ctypes.c_int))
