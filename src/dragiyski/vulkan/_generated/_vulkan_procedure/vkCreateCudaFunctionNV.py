import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCudaFunctionCreateInfoNV import VkCudaFunctionCreateInfoNV
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateCudaFunctionNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkCudaFunctionCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
