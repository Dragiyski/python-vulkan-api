import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderPassCreateInfo2 import VkRenderPassCreateInfo2
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateRenderPass2 = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderPassCreateInfo2), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
