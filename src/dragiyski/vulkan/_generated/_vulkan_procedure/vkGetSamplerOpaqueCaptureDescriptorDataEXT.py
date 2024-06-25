import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSamplerCaptureDescriptorDataInfoEXT import VkSamplerCaptureDescriptorDataInfoEXT

vkGetSamplerOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSamplerCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
