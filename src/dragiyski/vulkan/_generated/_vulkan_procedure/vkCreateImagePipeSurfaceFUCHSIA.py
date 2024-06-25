import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImagePipeSurfaceCreateInfoFUCHSIA import VkImagePipeSurfaceCreateInfoFUCHSIA
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateImagePipeSurfaceFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImagePipeSurfaceCreateInfoFUCHSIA), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
