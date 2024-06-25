import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDependencyInfo import VkDependencyInfo

vkCmdPipelineBarrier2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkDependencyInfo))
