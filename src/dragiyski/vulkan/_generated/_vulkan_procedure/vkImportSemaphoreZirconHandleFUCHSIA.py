import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkImportSemaphoreZirconHandleInfoFUCHSIA import VkImportSemaphoreZirconHandleInfoFUCHSIA

vkImportSemaphoreZirconHandleFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkImportSemaphoreZirconHandleInfoFUCHSIA))
