import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkViSurfaceCreateInfoNN import VkViSurfaceCreateInfoNN
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateViSurfaceNN = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkViSurfaceCreateInfoNN), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
