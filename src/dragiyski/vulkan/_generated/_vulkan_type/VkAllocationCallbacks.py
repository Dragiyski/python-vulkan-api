import ctypes

class CType(ctypes.Structure):
    pass

from ..vulkan_callback import vkAllocationFunction, vkFreeFunction, vkInternalAllocationNotification, vkInternalFreeNotification, vkReallocationFunction

CType._fields_ = [
    ('pUserData', ctypes.c_void_p),
    ('pfnAllocation', vkAllocationFunction),
    ('pfnReallocation', vkReallocationFunction),
    ('pfnFree', vkFreeFunction),
    ('pfnInternalAllocation', vkInternalAllocationNotification),
    ('pfnInternalFree', vkInternalFreeNotification),
]
