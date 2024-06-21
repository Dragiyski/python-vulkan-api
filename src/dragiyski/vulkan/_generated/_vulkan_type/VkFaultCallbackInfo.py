import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkFaultCallbackFunction
from .VkFaultData import CType as VkFaultData

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('faultCount', ctypes.c_uint32),
    ('pFaults', ctypes.POINTER(VkFaultData)),
    ('pfnFaultCallback', ctypes.POINTER(vkFaultCallbackFunction)),
]
