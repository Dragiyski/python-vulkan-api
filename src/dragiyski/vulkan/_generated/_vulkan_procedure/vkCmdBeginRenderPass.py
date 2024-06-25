import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderPassBeginInfo import VkRenderPassBeginInfo

vkCmdBeginRenderPass = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.c_int)
