import ctypes, sys

class VkGeometryDataNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkGeometryDataNV

from . import VkGeometryTrianglesNV
from . import VkGeometryAABBNV

VkGeometryDataNV._fields_ = [
    ('triangles', VkGeometryTrianglesNV),
    ('aabbs', VkGeometryAABBNV),
]
