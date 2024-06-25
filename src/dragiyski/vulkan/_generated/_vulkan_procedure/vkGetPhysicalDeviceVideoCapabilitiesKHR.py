import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoProfileInfoKHR import VkVideoProfileInfoKHR
from .._vulkan_type.VkVideoCapabilitiesKHR import VkVideoCapabilitiesKHR

vkGetPhysicalDeviceVideoCapabilitiesKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(VkVideoProfileInfoKHR), ctypes.POINTER(VkVideoCapabilitiesKHR))
