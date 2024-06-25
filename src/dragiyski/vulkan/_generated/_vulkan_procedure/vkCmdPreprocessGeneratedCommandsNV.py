import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkGeneratedCommandsInfoNV import VkGeneratedCommandsInfoNV

vkCmdPreprocessGeneratedCommandsNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkGeneratedCommandsInfoNV))
