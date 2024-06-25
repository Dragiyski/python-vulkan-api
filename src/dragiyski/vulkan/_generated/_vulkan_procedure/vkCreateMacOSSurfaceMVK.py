import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMacOSSurfaceCreateInfoMVK import VkMacOSSurfaceCreateInfoMVK
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateMacOSSurfaceMVK = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMacOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
