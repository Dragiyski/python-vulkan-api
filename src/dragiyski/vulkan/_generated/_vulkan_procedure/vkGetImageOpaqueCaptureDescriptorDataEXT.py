import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageCaptureDescriptorDataInfoEXT import VkImageCaptureDescriptorDataInfoEXT

vkGetImageOpaqueCaptureDescriptorDataEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImageCaptureDescriptorDataInfoEXT), ctypes.c_void_p)
