import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdSetFragmentShadingRateEnumNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_int, ctypes.ARRAY(ctypes.c_int, 2))
