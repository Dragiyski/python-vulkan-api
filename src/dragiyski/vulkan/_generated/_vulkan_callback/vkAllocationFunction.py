import ctypes
from ..vulkan_base import VKAPI_PTR


vkAllocationFunction = VKAPI_PTR(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int)
