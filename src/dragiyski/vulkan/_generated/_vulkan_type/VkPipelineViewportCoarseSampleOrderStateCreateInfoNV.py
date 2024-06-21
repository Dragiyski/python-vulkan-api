import ctypes

class CType(ctypes.Structure):
    pass

from .VkCoarseSampleOrderCustomNV import CType as VkCoarseSampleOrderCustomNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleOrderType', ctypes.c_int),
    ('customSampleOrderCount', ctypes.c_uint32),
    ('pCustomSampleOrders', ctypes.POINTER(VkCoarseSampleOrderCustomNV)),
]
