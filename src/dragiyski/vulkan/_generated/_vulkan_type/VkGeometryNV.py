import ctypes

class CType(ctypes.Structure):
    pass

from .VkGeometryDataNV import CType as VkGeometryDataNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkGeometryDataNV),
    ('flags', ctypes.c_uint32),
]
