import ctypes

class CType(ctypes.Structure):
    pass

from .VkGeometryAABBNV import CType as VkGeometryAABBNV
from .VkGeometryTrianglesNV import CType as VkGeometryTrianglesNV

CType._fields_ = [
    ('triangles', VkGeometryTrianglesNV),
    ('aabbs', VkGeometryAABBNV),
]
