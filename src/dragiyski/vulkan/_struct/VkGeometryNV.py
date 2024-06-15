import ctypes, sys

class VkGeometryNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkGeometryNV

from . import VkGeometryDataNV

VkGeometryNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkGeometryDataNV),
    ('flags', ctypes.c_uint32),
]
