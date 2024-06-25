import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSampleLocationsInfoEXT import VkSampleLocationsInfoEXT

vkCmdSetSampleLocationsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSampleLocationsInfoEXT))
