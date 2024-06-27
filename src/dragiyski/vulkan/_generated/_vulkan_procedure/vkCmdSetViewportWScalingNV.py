import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkViewportWScalingNV import VkViewportWScalingNV

vkCmdSetViewportWScalingNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkViewportWScalingNV))