import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkStridedDeviceAddressRegionKHR import VkStridedDeviceAddressRegionKHR
from .._vulkan_type.VkStridedDeviceAddressRegionKHR import VkStridedDeviceAddressRegionKHR
from .._vulkan_type.VkStridedDeviceAddressRegionKHR import VkStridedDeviceAddressRegionKHR
from .._vulkan_type.VkStridedDeviceAddressRegionKHR import VkStridedDeviceAddressRegionKHR

vkCmdTraceRaysKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.POINTER(VkStridedDeviceAddressRegionKHR), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
