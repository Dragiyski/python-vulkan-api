import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoSessionParametersCreateInfoKHR import VkVideoSessionParametersCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionParametersCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
