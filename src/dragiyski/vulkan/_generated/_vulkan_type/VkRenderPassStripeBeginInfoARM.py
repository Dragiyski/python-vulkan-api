import ctypes

class CType(ctypes.Structure):
    pass

from .VkRenderPassStripeInfoARM import CType as VkRenderPassStripeInfoARM

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeInfoCount', ctypes.c_uint32),
    ('pStripeInfos', ctypes.POINTER(VkRenderPassStripeInfoARM)),
]
