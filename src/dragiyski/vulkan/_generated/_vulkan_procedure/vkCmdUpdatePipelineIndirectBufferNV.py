import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdUpdatePipelineIndirectBufferNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
