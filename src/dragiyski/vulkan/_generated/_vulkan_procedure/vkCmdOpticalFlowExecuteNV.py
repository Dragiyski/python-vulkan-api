import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkOpticalFlowExecuteInfoNV import VkOpticalFlowExecuteInfoNV

vkCmdOpticalFlowExecuteNV = VKAPI_CALL(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkOpticalFlowExecuteInfoNV))
