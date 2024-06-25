import ctypes
from ..vulkan_base import VKAPI_CALL


vkAcquireFullScreenExclusiveModeEXT = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
