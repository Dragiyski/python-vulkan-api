import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkExtent2D import VkExtent2D

vkCmdSetFragmentShadingRateKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkExtent2D), ctypes.ARRAY(ctypes.c_int, 2))
