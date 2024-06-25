import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdSetDepthCompareOp = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int)
