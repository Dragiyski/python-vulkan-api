import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSubpassEndInfo import VkSubpassEndInfo

vkCmdEndRenderPass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSubpassEndInfo))
