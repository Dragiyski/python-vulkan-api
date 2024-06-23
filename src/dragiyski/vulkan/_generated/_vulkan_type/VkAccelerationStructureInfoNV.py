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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkGeometryNV',
    },
    'included_in': {
        'VkAccelerationStructureCreateInfoNV',
    },
    'input_of': {
        'vkCmdBuildAccelerationStructureNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACCELERATION_STRUCTURE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'type': {'python_name': ['type'], 'type': 'VkAccelerationStructureTypeKHR'},
        'flags': {'python_name': ['flags'], 'type': 'VkBuildAccelerationStructureFlagsKHR'},
        'instanceCount': {'python_name': ['instance', 'count']},
        'geometryCount': {'python_name': ['geometry', 'count']},
        'pGeometries': {'python_name': ['p', 'geometries'], 'len': [['geometryCount']], 'type': 'VkGeometryNV'},
    }
}
