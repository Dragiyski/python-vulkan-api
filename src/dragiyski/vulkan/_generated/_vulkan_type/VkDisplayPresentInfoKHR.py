import ctypes

class VkDisplayPresentInfoKHR(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D

VkDisplayPresentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcRect', VkRect2D),
    ('dstRect', VkRect2D),
    ('persistent', ctypes.c_uint32),
]

VkDisplayPresentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcRect': VkRect2D,
    'dstRect': VkRect2D,
    'persistent': ctypes.c_uint32,
}
