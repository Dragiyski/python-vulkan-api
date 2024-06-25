import ctypes

class VkGeometryDataNV(ctypes.Structure):
    pass

from .VkGeometryAABBNV import VkGeometryAABBNV
from .VkGeometryTrianglesNV import VkGeometryTrianglesNV

VkGeometryDataNV._fields_ = [
    ('triangles', VkGeometryTrianglesNV),
    ('aabbs', VkGeometryAABBNV),
]

VkGeometryDataNV._type_ = {
    'triangles': VkGeometryTrianglesNV,
    'aabbs': VkGeometryAABBNV,
}
