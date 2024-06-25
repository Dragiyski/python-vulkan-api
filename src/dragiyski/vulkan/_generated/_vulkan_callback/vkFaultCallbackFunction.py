import ctypes
from ..vulkan_base import VKAPI_PTR

from .._vulkan_type.VkFaultData import VkFaultData

vkFaultCallbackFunction = VKAPI_PTR(None, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(VkFaultData))
