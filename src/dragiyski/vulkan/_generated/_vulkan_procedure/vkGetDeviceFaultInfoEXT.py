import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceFaultCountsEXT import VkDeviceFaultCountsEXT
from .._vulkan_type.VkDeviceFaultInfoEXT import VkDeviceFaultInfoEXT

vkGetDeviceFaultInfoEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceFaultCountsEXT), ctypes.POINTER(VkDeviceFaultInfoEXT))
