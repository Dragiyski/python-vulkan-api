import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('deviceIndexCount', ctypes.c_uint32),
    ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ('splitInstanceBindRegionCount', ctypes.c_uint32),
    ('pSplitInstanceBindRegions', ctypes.POINTER(VkRect2D)),
]
