import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceEventInfoEXT import VkDeviceEventInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkRegisterDeviceEventEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
