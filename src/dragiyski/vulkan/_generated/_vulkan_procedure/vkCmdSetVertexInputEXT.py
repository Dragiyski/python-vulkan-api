import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVertexInputBindingDescription2EXT import VkVertexInputBindingDescription2EXT
from .._vulkan_type.VkVertexInputAttributeDescription2EXT import VkVertexInputAttributeDescription2EXT

vkCmdSetVertexInputEXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_uint32, ctypes.POINTER(VkVertexInputBindingDescription2EXT), ctypes.c_uint32, ctypes.POINTER(VkVertexInputAttributeDescription2EXT))
