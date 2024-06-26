import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAccelerationStructureBuildGeometryInfoKHR import VkAccelerationStructureBuildGeometryInfoKHR
from .._vulkan_type.VkAccelerationStructureBuildRangeInfoKHR import VkAccelerationStructureBuildRangeInfoKHR

vkCmdBuildAccelerationStructuresKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkAccelerationStructureBuildGeometryInfoKHR), ctypes.POINTER(ctypes.POINTER(VkAccelerationStructureBuildRangeInfoKHR)))
