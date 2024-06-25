import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMultiDrawInfoEXT import VkMultiDrawInfoEXT

vkCmdDrawMultiEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultiDrawInfoEXT), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
