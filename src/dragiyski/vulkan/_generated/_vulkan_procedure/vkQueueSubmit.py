import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSubmitInfo import VkSubmitInfo

vkQueueSubmit = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkSubmitInfo), ctypes.c_void_p)
