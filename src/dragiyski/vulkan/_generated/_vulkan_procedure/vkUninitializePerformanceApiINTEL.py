import ctypes
from ..vulkan_base import VKAPI_CALL


vkUninitializePerformanceApiINTEL = VKAPI_CALL(None, ctypes.c_void_p)
