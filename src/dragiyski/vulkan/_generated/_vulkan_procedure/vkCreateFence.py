import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkFenceCreateInfo import VkFenceCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateFence = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkFenceCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
