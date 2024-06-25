import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAccelerationStructureCreateInfoKHR import VkAccelerationStructureCreateInfoKHR
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateAccelerationStructureKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureCreateInfoKHR), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
