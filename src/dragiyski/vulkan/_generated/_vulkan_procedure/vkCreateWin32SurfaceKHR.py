import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkWin32SurfaceCreateInfoKHR import VkWin32SurfaceCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateWin32SurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkWin32SurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
