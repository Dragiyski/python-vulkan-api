import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkSemaphoreCreateInfo import VkSemaphoreCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateSemaphore = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkSemaphoreCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
