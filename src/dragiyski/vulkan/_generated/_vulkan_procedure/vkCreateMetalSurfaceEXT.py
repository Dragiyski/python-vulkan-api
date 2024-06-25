import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMetalSurfaceCreateInfoEXT import VkMetalSurfaceCreateInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateMetalSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMetalSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
