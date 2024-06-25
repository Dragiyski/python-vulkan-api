import ctypes

class VkRenderPassStripeInfoARM(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D

VkRenderPassStripeInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeArea', VkRect2D),
]

VkRenderPassStripeInfoARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stripeArea': VkRect2D,
}
