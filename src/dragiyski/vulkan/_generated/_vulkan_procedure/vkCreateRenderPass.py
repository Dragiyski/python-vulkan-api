import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderPassCreateInfo import VkRenderPassCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateRenderPass = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkRenderPassCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
