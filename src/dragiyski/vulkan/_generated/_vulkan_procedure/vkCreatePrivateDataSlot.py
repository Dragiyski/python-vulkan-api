import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkPrivateDataSlotCreateInfo import VkPrivateDataSlotCreateInfo
from .._vulkan_type.VkAllocationCallbacks import VkAllocationCallbacks

vkCreatePrivateDataSlot = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkPrivateDataSlotCreateInfo), ctypes.POINTER(VkAllocationCallbacks), ctypes.POINTER(ctypes.c_void_p))
