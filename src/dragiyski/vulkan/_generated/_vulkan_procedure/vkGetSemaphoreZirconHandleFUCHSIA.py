import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSemaphoreGetZirconHandleInfoFUCHSIA import VkSemaphoreGetZirconHandleInfoFUCHSIA

vkGetSemaphoreZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreGetZirconHandleInfoFUCHSIA), ctypes.POINTER(ctypes.c_uint32))
