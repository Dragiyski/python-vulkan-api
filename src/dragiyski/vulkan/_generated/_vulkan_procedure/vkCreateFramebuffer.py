import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkFramebufferCreateInfo import VkFramebufferCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateFramebuffer = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFramebufferCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
