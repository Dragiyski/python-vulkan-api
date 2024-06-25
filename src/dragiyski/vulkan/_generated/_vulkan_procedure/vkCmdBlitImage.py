import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImageBlit import VkImageBlit

vkCmdBlitImage = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(VkImageBlit), ctypes.c_int)
