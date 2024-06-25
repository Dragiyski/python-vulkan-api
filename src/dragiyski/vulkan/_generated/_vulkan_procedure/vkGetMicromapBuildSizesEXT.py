import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMicromapBuildInfoEXT import VkMicromapBuildInfoEXT
from .._vulkan_type.VkMicromapBuildSizesInfoEXT import VkMicromapBuildSizesInfoEXT

vkGetMicromapBuildSizesEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(VkMicromapBuildInfoEXT), ctypes.POINTER(VkMicromapBuildSizesInfoEXT))
