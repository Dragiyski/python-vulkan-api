import ctypes

class CType(ctypes.Structure):
    pass

from .VkGeometryNV import CType as VkGeometryNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('flags', ctypes.c_uint32),
    ('instanceCount', ctypes.c_uint32),
    ('geometryCount', ctypes.c_uint32),
    ('pGeometries', ctypes.POINTER(VkGeometryNV)),
]
