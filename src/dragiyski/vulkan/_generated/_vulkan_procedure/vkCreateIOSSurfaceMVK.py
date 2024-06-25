import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkIOSSurfaceCreateInfoMVK import VkIOSSurfaceCreateInfoMVK
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateIOSSurfaceMVK = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkIOSSurfaceCreateInfoMVK), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
