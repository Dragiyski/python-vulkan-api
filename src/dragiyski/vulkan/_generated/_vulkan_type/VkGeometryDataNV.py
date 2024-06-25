import ctypes

class VkGeometryDataNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'triangles': VkGeometryTrianglesNV,
            'aabbs': VkGeometryAABBNV,
        }


from .VkGeometryAABBNV import VkGeometryAABBNV
from .VkGeometryTrianglesNV import VkGeometryTrianglesNV

VkGeometryDataNV._fields_ = [
    ('triangles', VkGeometryTrianglesNV),
    ('aabbs', VkGeometryAABBNV),
]
