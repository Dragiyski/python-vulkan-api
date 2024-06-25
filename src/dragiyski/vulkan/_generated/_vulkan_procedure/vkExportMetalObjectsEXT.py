import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkExportMetalObjectsInfoEXT import VkExportMetalObjectsInfoEXT

vkExportMetalObjectsEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkExportMetalObjectsInfoEXT))
