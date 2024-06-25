import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkVideoSessionParametersUpdateInfoKHR import VkVideoSessionParametersUpdateInfoKHR

vkUpdateVideoSessionParametersKHR = VKAPI_CALL(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(VkVideoSessionParametersUpdateInfoKHR))
