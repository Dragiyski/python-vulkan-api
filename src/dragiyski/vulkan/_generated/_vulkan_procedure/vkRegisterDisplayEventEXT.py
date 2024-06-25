import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDisplayEventInfoEXT import VkDisplayEventInfoEXT
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkRegisterDisplayEventEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkDisplayEventInfoEXT), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
