import ctypes

class VkAllocationCallbacks(ctypes.Structure):
    pass

from .._vulkan_callback.vkAllocationFunction import vkAllocationFunction
from .._vulkan_callback.vkFreeFunction import vkFreeFunction
from .._vulkan_callback.vkInternalAllocationNotification import vkInternalAllocationNotification
from .._vulkan_callback.vkInternalFreeNotification import vkInternalFreeNotification
from .._vulkan_callback.vkReallocationFunction import vkReallocationFunction

VkAllocationCallbacks._fields_ = [
    ('pUserData', ctypes.c_void_p),
    ('pfnAllocation', vkAllocationFunction),
    ('pfnReallocation', vkReallocationFunction),
    ('pfnFree', vkFreeFunction),
    ('pfnInternalAllocation', vkInternalAllocationNotification),
    ('pfnInternalFree', vkInternalFreeNotification),
]

VkAllocationCallbacks._type_ = {
    'pUserData': ctypes.c_void_p,
    'pfnAllocation': vkAllocationFunction,
    'pfnReallocation': vkReallocationFunction,
    'pfnFree': vkFreeFunction,
    'pfnInternalAllocation': vkInternalAllocationNotification,
    'pfnInternalFree': vkInternalFreeNotification,
}
