import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdSetDepthBias = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)
