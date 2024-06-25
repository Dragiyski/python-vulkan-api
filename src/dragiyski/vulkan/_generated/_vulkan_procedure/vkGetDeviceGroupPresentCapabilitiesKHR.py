import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkDeviceGroupPresentCapabilitiesKHR import VkDeviceGroupPresentCapabilitiesKHR

vkGetDeviceGroupPresentCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkDeviceGroupPresentCapabilitiesKHR))
