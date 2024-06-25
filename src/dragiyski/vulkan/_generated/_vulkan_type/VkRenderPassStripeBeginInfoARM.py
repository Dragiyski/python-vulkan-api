import ctypes

class VkRenderPassStripeBeginInfoARM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stripeInfoCount': ctypes.c_uint32,
            'pStripeInfos': ctypes.POINTER(VkRenderPassStripeInfoARM),
        }


from .VkRenderPassStripeInfoARM import VkRenderPassStripeInfoARM

VkRenderPassStripeBeginInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeInfoCount', ctypes.c_uint32),
    ('pStripeInfos', ctypes.POINTER(VkRenderPassStripeInfoARM)),
]
