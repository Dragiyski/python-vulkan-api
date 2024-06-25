import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAccelerationStructureVersionInfoKHR import VkAccelerationStructureVersionInfoKHR

vkGetDeviceAccelerationStructureCompatibilityKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureVersionInfoKHR), ctypes.POINTER(ctypes.c_int))
