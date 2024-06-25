import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMultiDrawIndexedInfoEXT import VkMultiDrawIndexedInfoEXT

vkCmdDrawMultiIndexedEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultiDrawIndexedInfoEXT), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int32))
