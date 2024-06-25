import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBufferCollectionCreateInfoFUCHSIA import VkBufferCollectionCreateInfoFUCHSIA
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreateBufferCollectionFUCHSIA = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkBufferCollectionCreateInfoFUCHSIA), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
