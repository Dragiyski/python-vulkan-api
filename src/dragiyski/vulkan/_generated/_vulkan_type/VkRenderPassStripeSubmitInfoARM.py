import ctypes, sys

class VkRenderPassStripeSubmitInfoARM(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassStripeSubmitInfoARM

from . import VkSemaphoreSubmitInfo

VkRenderPassStripeSubmitInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeSemaphoreInfoCount', ctypes.c_uint32),
    ('pStripeSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
]
