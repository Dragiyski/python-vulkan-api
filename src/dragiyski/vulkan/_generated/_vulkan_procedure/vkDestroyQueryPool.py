import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkDestroyQueryPool = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkAllocationCallbacks))
