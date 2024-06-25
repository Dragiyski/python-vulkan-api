import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageViewHandleInfoNVX import VkImageViewHandleInfoNVX

vkGetImageViewHandleNVX = VKAPI_CALL(ctypes.c_uint32, ctypes.c_void_p, ctypes.POINTER(VkImageViewHandleInfoNVX))
