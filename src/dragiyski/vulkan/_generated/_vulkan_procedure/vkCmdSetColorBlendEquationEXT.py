import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkColorBlendEquationEXT import VkColorBlendEquationEXT

vkCmdSetColorBlendEquationEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkColorBlendEquationEXT))
