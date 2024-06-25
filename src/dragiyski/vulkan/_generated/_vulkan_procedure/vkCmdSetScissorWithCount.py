import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRect2D import VkRect2D

vkCmdSetScissorWithCount = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkRect2D))
