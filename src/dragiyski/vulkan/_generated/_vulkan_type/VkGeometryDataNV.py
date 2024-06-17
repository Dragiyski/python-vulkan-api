import ctypes, sys

class VkGeometryDataNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkGeometryDataNV

from . import VkGeometryAABBNV
from . import VkGeometryTrianglesNV

VkGeometryDataNV._fields_ = [
    ('triangles', VkGeometryTrianglesNV),
    ('aabbs', VkGeometryAABBNV),
]
