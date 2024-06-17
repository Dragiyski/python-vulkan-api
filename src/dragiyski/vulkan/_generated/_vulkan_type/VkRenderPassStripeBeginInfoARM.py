import ctypes, sys

class VkRenderPassStripeBeginInfoARM(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassStripeBeginInfoARM

from . import VkRenderPassStripeInfoARM

VkRenderPassStripeBeginInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeInfoCount', ctypes.c_uint32),
    ('pStripeInfos', ctypes.POINTER(VkRenderPassStripeInfoARM)),
]
