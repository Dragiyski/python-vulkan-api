import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAccelerationStructureCreateInfoNV import VkAccelerationStructureCreateInfoNV
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateAccelerationStructureNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
