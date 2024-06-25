import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdEndDebugUtilsLabelEXT = VKAPI_CALL(None, ctypes.c_void_p)
