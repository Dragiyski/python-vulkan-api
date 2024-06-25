import ctypes

class VkRenderPassStripeInfoARM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stripeArea': VkRect2D,
        }


from .VkRect2D import VkRect2D

VkRenderPassStripeInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeArea', VkRect2D),
]
