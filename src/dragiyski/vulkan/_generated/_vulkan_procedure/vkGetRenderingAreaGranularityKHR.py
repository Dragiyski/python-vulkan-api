import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderingAreaInfoKHR import VkRenderingAreaInfoKHR
from .._vulkan_type.VkExtent2D import VkExtent2D

vkGetRenderingAreaGranularityKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingAreaInfoKHR), ctypes.POINTER(VkExtent2D))
