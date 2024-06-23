import ctypes

class CType(ctypes.Structure):
    pass

from .VkGeometryAABBNV import CType as VkGeometryAABBNV
from .VkGeometryTrianglesNV import CType as VkGeometryTrianglesNV

CType._fields_ = [
    ('triangles', VkGeometryTrianglesNV),
    ('aabbs', VkGeometryAABBNV),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkGeometryAABBNV',
        'VkGeometryTrianglesNV',
    },
    'included_in': {
        'VkGeometryNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'triangles': {'python_name': ['triangles'], 'type': 'VkGeometryTrianglesNV'},
        'aabbs': {'python_name': ['aabbs'], 'type': 'VkGeometryAABBNV'},
    }
}
