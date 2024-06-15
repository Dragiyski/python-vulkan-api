import ctypes, sys

class VkRenderPassStripeInfoARM(ctypes.Structure):
    pass

sys.modules[__name__] = VkRenderPassStripeInfoARM

from . import VkRect2D

VkRenderPassStripeInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeArea', VkRect2D),
]
