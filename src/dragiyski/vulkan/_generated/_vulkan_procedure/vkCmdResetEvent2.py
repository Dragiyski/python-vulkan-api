import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdResetEvent2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64)
