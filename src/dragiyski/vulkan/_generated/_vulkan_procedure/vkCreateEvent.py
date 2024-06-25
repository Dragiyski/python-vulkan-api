import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkEventCreateInfo import VkEventCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateEvent = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkEventCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
