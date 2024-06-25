import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPipelineIndirectDeviceAddressInfoNV import VkPipelineIndirectDeviceAddressInfoNV

vkGetPipelineIndirectDeviceAddressNV = VKAPI_CALL(ctypes.c_uint64, ctypes.c_void_p, ctypes.POINTER(VkPipelineIndirectDeviceAddressInfoNV))
