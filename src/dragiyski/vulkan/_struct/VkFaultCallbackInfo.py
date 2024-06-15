import ctypes, sys

class VkFaultCallbackInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkFaultCallbackInfo

from .._vulkan_callback import vkFaultCallbackFunction
from . import VkFaultData

VkFaultCallbackInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('faultCount', ctypes.c_uint32),
    ('pFaults', ctypes.POINTER(VkFaultData)),
    ('pfnFaultCallback', ctypes.POINTER(vkFaultCallbackFunction)),
]
