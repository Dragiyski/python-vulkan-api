import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryGetSciBufInfoNV import VkMemoryGetSciBufInfoNV

vkGetMemorySciBufNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetSciBufInfoNV), ctypes.POINTER(ctypes.c_void_p))
