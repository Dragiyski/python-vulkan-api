import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkMemoryGetAndroidHardwareBufferInfoANDROID import VkMemoryGetAndroidHardwareBufferInfoANDROID

vkGetMemoryAndroidHardwareBufferANDROID = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkMemoryGetAndroidHardwareBufferInfoANDROID), ctypes.POINTER(ctypes.c_void_p))
