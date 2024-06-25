import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdEndRendering = VKAPI_CALL(None, ctypes.c_void_p)
