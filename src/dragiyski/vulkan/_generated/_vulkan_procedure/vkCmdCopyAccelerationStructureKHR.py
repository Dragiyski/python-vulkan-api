import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkCopyAccelerationStructureInfoKHR import VkCopyAccelerationStructureInfoKHR

vkCmdCopyAccelerationStructureKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkCopyAccelerationStructureInfoKHR))
