import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDescriptorGetInfoEXT import VkDescriptorGetInfoEXT

vkGetDescriptorEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDescriptorGetInfoEXT), ctypes.c_size_t, ctypes.c_void_p)
