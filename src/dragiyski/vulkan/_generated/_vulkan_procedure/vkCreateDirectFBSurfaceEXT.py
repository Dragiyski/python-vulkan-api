import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDirectFBSurfaceCreateInfoEXT import VkDirectFBSurfaceCreateInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateDirectFBSurfaceEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDirectFBSurfaceCreateInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
