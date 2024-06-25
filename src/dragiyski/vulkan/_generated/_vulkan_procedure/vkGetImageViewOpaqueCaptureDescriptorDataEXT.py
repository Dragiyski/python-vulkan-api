import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageViewCaptureDescriptorDataInfoEXT import VkImageViewCaptureDescriptorDataInfoEXT

vkGetImageViewOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageViewCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
