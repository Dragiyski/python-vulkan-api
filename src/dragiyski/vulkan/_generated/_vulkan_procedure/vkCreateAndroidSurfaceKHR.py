import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAndroidSurfaceCreateInfoKHR import VkAndroidSurfaceCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateAndroidSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAndroidSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
