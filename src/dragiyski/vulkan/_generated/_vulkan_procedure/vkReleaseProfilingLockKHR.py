import ctypes
from ..vulkan_base import VKAPI_CALL


vkReleaseProfilingLockKHR = VKAPI_CALL(None, ctypes.c_void_p)
