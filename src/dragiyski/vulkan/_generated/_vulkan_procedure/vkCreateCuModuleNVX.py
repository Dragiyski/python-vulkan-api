import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCuModuleCreateInfoNVX import VkCuModuleCreateInfoNVX
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateCuModuleNVX = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCuModuleCreateInfoNVX), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
