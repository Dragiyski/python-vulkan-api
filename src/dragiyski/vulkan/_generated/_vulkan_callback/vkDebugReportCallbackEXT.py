import ctypes
from ..vulkan_base import VKAPI_PTR


vkDebugReportCallbackEXT = VKAPI_PTR(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint64, ctypes.c_size_t, ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)
