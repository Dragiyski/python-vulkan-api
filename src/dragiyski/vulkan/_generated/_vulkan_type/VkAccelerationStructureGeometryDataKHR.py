import ctypes

class CType(ctypes.Union):
    pass

from .VkAccelerationStructureGeometryAabbsDataKHR import CType as VkAccelerationStructureGeometryAabbsDataKHR
from .VkAccelerationStructureGeometryInstancesDataKHR import CType as VkAccelerationStructureGeometryInstancesDataKHR
from .VkAccelerationStructureGeometryTrianglesDataKHR import CType as VkAccelerationStructureGeometryTrianglesDataKHR

CType._fields_ = [
    ('triangles', VkAccelerationStructureGeometryTrianglesDataKHR),
    ('aabbs', VkAccelerationStructureGeometryAabbsDataKHR),
    ('instances', VkAccelerationStructureGeometryInstancesDataKHR),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkAccelerationStructureGeometryAabbsDataKHR',
        'VkAccelerationStructureGeometryInstancesDataKHR',
        'VkAccelerationStructureGeometryTrianglesDataKHR',
    },
    'included_in': {
        'VkAccelerationStructureGeometryKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'triangles': {'python_name': ['triangles'], 'type': 'VkAccelerationStructureGeometryTrianglesDataKHR'},
        'aabbs': {'python_name': ['aabbs'], 'type': 'VkAccelerationStructureGeometryAabbsDataKHR'},
        'instances': {'python_name': ['instances'], 'type': 'VkAccelerationStructureGeometryInstancesDataKHR'},
    }
}
