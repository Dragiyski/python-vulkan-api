import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderPassBeginInfo import VkRenderPassBeginInfo
from .._vulkan_type.VkSubpassBeginInfo import VkSubpassBeginInfo

vkCmdBeginRenderPass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderPassBeginInfo), ctypes.POINTER(VkSubpassBeginInfo))
