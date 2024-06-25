import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdSetCullMode = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)
