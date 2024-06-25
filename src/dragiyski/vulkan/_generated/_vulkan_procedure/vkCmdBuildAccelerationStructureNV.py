import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAccelerationStructureInfoNV import VkAccelerationStructureInfoNV

vkCmdBuildAccelerationStructureNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkAccelerationStructureInfoNV), ctypes.c_void_p, ctypes.c_uint64, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
