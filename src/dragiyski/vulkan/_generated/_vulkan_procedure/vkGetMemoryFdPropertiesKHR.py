import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryFdPropertiesKHR import VkMemoryFdPropertiesKHR

vkGetMemoryFdPropertiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.POINTER(VkMemoryFdPropertiesKHR))
