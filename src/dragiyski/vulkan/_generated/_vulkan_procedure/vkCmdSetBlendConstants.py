import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdSetBlendConstants = VKAPI_CALL(None, ctypes.c_void_p, ctypes.ARRAY(ctypes.c_float, 4))
