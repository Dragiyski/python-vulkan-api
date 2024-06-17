import ctypes, sys

class VkAllocationCallbacks(ctypes.Structure):
    pass

sys.modules[__name__] = VkAllocationCallbacks

from ..vulkan_callback import vkAllocationFunction, vkFreeFunction, vkInternalAllocationNotification, vkInternalFreeNotification, vkReallocationFunction

VkAllocationCallbacks._fields_ = [
    ('pUserData', ctypes.c_void_p),
    ('pfnAllocation', ctypes.POINTER(vkAllocationFunction)),
    ('pfnReallocation', ctypes.POINTER(vkReallocationFunction)),
    ('pfnFree', ctypes.POINTER(vkFreeFunction)),
    ('pfnInternalAllocation', ctypes.POINTER(vkInternalAllocationNotification)),
    ('pfnInternalFree', ctypes.POINTER(vkInternalFreeNotification)),
]
