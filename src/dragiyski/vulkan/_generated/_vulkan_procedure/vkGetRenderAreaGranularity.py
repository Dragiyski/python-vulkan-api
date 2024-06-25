import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkExtent2D import VkExtent2D

vkGetRenderAreaGranularity = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkExtent2D))
