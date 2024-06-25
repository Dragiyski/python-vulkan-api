import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkIndirectCommandsLayoutCreateInfoNV import VkIndirectCommandsLayoutCreateInfoNV
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateIndirectCommandsLayoutNV = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkIndirectCommandsLayoutCreateInfoNV), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
