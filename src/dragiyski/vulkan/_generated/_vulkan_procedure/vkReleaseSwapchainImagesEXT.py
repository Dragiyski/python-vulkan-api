import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkReleaseSwapchainImagesInfoEXT import VkReleaseSwapchainImagesInfoEXT

vkReleaseSwapchainImagesEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkReleaseSwapchainImagesInfoEXT))
