import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdEndConditionalRenderingEXT = VKAPI_CALL(None, ctypes.c_void_p)
