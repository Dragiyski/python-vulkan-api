import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDebugMarkerObjectNameInfoEXT import VkDebugMarkerObjectNameInfoEXT

vkDebugMarkerSetObjectNameEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDebugMarkerObjectNameInfoEXT))
