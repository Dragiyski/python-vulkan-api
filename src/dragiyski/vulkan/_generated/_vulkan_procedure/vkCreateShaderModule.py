import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkShaderModuleCreateInfo import VkShaderModuleCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateShaderModule = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkShaderModuleCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
