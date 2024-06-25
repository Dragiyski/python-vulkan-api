import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoSessionCreateInfoKHR import VkVideoSessionCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateVideoSessionKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
