import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkXlibSurfaceCreateInfoKHR import VkXlibSurfaceCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateXlibSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkXlibSurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
