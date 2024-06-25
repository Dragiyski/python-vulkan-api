import ctypes
from ..vulkan_base import VKAPI_CALL


vkSetDeviceMemoryPriorityEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)
