import ctypes

class VkFaultCallbackInfo(ctypes.Structure):
    pass

from .._vulkan_callback.vkFaultCallbackFunction import vkFaultCallbackFunction
from .VkFaultData import VkFaultData

VkFaultCallbackInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('faultCount', ctypes.c_uint32),
    ('pFaults', ctypes.POINTER(VkFaultData)),
    ('pfnFaultCallback', vkFaultCallbackFunction),
]

VkFaultCallbackInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'faultCount': ctypes.c_uint32,
    'pFaults': ctypes.POINTER(VkFaultData),
    'pfnFaultCallback': vkFaultCallbackFunction,
}
