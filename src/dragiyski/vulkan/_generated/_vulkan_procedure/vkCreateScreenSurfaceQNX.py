import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkScreenSurfaceCreateInfoQNX import VkScreenSurfaceCreateInfoQNX
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateScreenSurfaceQNX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkScreenSurfaceCreateInfoQNX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
