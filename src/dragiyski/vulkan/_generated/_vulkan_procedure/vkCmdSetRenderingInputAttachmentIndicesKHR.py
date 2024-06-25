import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRenderingInputAttachmentIndexInfoKHR import VkRenderingInputAttachmentIndexInfoKHR

vkCmdSetRenderingInputAttachmentIndicesKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRenderingInputAttachmentIndexInfoKHR))
