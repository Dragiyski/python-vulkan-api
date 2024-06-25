import ctypes

class VkRenderPassStripeSubmitInfoARM(ctypes.Structure):
    pass

from .VkSemaphoreSubmitInfo import VkSemaphoreSubmitInfo

VkRenderPassStripeSubmitInfoARM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stripeSemaphoreInfoCount', ctypes.c_uint32),
    ('pStripeSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
]

VkRenderPassStripeSubmitInfoARM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stripeSemaphoreInfoCount': ctypes.c_uint32,
    'pStripeSemaphoreInfos': ctypes.POINTER(VkSemaphoreSubmitInfo),
}
