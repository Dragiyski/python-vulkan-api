import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdSetColorWriteEnableEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
