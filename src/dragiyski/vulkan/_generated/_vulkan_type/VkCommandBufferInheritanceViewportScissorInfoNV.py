import ctypes

class CType(ctypes.Structure):
    pass

from .VkViewport import CType as VkViewport

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportScissor2D', ctypes.c_uint32),
    ('viewportDepthCount', ctypes.c_uint32),
    ('pViewportDepths', ctypes.POINTER(VkViewport)),
]
