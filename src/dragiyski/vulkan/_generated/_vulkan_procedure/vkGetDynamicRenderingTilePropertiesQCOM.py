import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderingInfo import VkRenderingInfo
from .._vulkan_type.VkTilePropertiesQCOM import VkTilePropertiesQCOM

vkGetDynamicRenderingTilePropertiesQCOM = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderingInfo), ctypes.POINTER(VkTilePropertiesQCOM))
