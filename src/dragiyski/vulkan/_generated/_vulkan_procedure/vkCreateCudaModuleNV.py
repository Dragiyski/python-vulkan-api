import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCudaModuleCreateInfoNV import VkCudaModuleCreateInfoNV
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateCudaModuleNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCudaModuleCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
