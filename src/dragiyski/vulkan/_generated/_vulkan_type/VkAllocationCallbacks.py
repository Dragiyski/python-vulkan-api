import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkAllocationFunction, vkFreeFunction, vkInternalAllocationNotification, vkInternalFreeNotification, vkReallocationFunction

CType._fields_ = [
    ('pUserData', ctypes.c_void_p),
    ('pfnAllocation', ctypes.POINTER(vkAllocationFunction)),
    ('pfnReallocation', ctypes.POINTER(vkReallocationFunction)),
    ('pfnFree', ctypes.POINTER(vkFreeFunction)),
    ('pfnInternalAllocation', ctypes.POINTER(vkInternalAllocationNotification)),
    ('pfnInternalFree', ctypes.POINTER(vkInternalFreeNotification)),
]
