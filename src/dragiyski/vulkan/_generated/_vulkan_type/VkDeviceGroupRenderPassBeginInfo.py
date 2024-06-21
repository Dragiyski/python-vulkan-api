import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceMask', ctypes.c_uint32),
    ('deviceRenderAreaCount', ctypes.c_uint32),
    ('pDeviceRenderAreas', ctypes.POINTER(VkRect2D)),
]
