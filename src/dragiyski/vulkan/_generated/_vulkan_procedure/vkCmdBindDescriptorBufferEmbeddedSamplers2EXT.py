import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkBindDescriptorBufferEmbeddedSamplersInfoEXT import VkBindDescriptorBufferEmbeddedSamplersInfoEXT

vkCmdBindDescriptorBufferEmbeddedSamplers2EXT = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkBindDescriptorBufferEmbeddedSamplersInfoEXT))
