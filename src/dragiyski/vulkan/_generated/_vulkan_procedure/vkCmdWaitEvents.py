import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryBarrier import VkMemoryBarrier
from .._vulkan_type.VkBufferMemoryBarrier import VkBufferMemoryBarrier
from .._vulkan_type.VkImageMemoryBarrier import VkImageMemoryBarrier

vkCmdWaitEvents = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkBufferMemoryBarrier), ctypes.c_uint32, ctypes.POINTER(VkImageMemoryBarrier))
