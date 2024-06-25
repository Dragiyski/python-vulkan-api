import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBufferDeviceAddressInfo import VkBufferDeviceAddressInfo

vkGetBufferDeviceAddress = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkBufferDeviceAddressInfo))
