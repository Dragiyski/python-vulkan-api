import ctypes
from ..vulkan_base import VKAPI_PTR


vkInternalAllocationNotification = VKAPI_PTR(None, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int, ctypes.c_int)
