import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCuFunctionCreateInfoNVX import VkCuFunctionCreateInfoNVX
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateCuFunctionNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCuFunctionCreateInfoNVX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
