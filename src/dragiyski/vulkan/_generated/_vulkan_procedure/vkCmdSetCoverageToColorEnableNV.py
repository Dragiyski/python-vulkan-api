import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdSetCoverageToColorEnableNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32)