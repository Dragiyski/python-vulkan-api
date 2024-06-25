import ctypes

class VkRenderPassStripeSubmitInfoARM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stripeSemaphoreInfoCount': ctypes.c_uint32,
            'pStripeSemaphoreInfos': ctypes.POINTER(VkSemaphoreSubmitInfo),
        }


from .VkSemaphoreSubmitInfo import VkSemaphoreSubmitInfo

VkRenderPassStripeSubmitInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeSemaphoreInfoCount', ctypes.c_uint32),
    ('pStripeSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
]
