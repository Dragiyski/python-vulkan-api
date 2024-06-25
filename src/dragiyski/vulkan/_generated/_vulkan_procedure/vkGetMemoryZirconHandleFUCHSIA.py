import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryGetZirconHandleInfoFUCHSIA import VkMemoryGetZirconHandleInfoFUCHSIA

vkGetMemoryZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetZirconHandleInfoFUCHSIA), ctypes.POINTER(ctypes.c_uint32))
