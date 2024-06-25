import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderingInfo import VkRenderingInfo

vkCmdBeginRendering = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingInfo))
