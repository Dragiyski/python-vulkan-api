import ctypes
from ..vulkan_base import VKAPI_CALL


vkGetDeviceGroupSurfacePresentModesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32))
