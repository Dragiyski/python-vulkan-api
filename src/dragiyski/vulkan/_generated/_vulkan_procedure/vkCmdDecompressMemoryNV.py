import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDecompressMemoryRegionNV import VkDecompressMemoryRegionNV

vkCmdDecompressMemoryNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkDecompressMemoryRegionNV))
