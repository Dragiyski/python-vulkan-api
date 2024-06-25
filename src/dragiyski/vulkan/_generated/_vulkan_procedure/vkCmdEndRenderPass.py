import ctypes
from ..vulkan_base import VKAPI_CALL


vkCmdEndRenderPass = VKAPI_CALL(None, ctypes.c_void_p)
