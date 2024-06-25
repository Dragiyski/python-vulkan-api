import ctypes

class VkRenderPassStripeBeginInfoARM(ctypes.Structure):
    pass

from .VkRenderPassStripeInfoARM import VkRenderPassStripeInfoARM

VkRenderPassStripeBeginInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeInfoCount', ctypes.c_uint32),
    ('pStripeInfos', ctypes.POINTER(VkRenderPassStripeInfoARM)),
]

VkRenderPassStripeBeginInfoARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stripeInfoCount': ctypes.c_uint32,
    'pStripeInfos': ctypes.POINTER(VkRenderPassStripeInfoARM),
}
