import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyMemoryToAccelerationStructureInfoKHR import VkCopyMemoryToAccelerationStructureInfoKHR

vkCmdCopyMemoryToAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyMemoryToAccelerationStructureInfoKHR))
