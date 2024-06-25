import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMultisamplePropertiesEXT import VkMultisamplePropertiesEXT

vkGetPhysicalDeviceMultisamplePropertiesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkMultisamplePropertiesEXT))
