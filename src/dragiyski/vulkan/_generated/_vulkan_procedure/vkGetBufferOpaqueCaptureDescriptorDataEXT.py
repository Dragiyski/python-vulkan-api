import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBufferCaptureDescriptorDataInfoEXT import VkBufferCaptureDescriptorDataInfoEXT

vkGetBufferOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
