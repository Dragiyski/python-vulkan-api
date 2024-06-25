import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplaySurfaceCreateInfoKHR import VkDisplaySurfaceCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDisplayPlaneSurfaceKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDisplaySurfaceCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
