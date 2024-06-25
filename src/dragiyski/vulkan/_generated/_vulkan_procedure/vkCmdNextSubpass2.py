import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSubpassBeginInfo import VkSubpassBeginInfo
from .._vulkan_type.VkSubpassEndInfo import VkSubpassEndInfo

vkCmdNextSubpass2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkSubpassBeginInfo), ctypes.POINTER(VkSubpassEndInfo))
