import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkStreamDescriptorSurfaceCreateInfoGGP import VkStreamDescriptorSurfaceCreateInfoGGP
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateStreamDescriptorSurfaceGGP = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkStreamDescriptorSurfaceCreateInfoGGP), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
