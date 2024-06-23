import ctypes

class CType(ctypes.Structure):
    pass

from .VkAccelerationStructureGeometryDataKHR import CType as VkAccelerationStructureGeometryDataKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkAccelerationStructureGeometryDataKHR),
    ('flags', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkAccelerationStructureGeometryDataKHR',
    },
    'included_in': {
        'VkAccelerationStructureBuildGeometryInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_GEOMETRY_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'geometryType': {'python_name': ['geometry', 'type'], 'type': 'VkGeometryTypeKHR'},
        'geometry': {'python_name': ['geometry'], 'type': 'VkAccelerationStructureGeometryDataKHR'},
        'flags': {'python_name': ['flags'], 'type': 'VkGeometryFlagsKHR'},
    }
}
