import ctypes
from ..vulkan_base import VKAPI_CALL

from .._vulkan_type.VkRefreshObjectListKHR import VkRefreshObjectListKHR

vkCmdRefreshObjectsKHR = VKAPI_CALL(None, ctypes.c_void_p, ctypes.POINTER(VkRefreshObjectListKHR))
