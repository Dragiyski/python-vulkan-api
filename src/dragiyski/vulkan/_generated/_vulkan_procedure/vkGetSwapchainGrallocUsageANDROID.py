import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetSwapchainGrallocUsageANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.POINTER(ctypes.c_int))
