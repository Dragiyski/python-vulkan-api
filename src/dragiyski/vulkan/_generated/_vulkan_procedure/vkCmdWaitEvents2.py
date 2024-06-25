import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDependencyInfo import VkDependencyInfo

vkCmdWaitEvents2 = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(VkDependencyInfo))
