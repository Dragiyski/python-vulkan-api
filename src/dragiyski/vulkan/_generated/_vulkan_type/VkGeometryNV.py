import ctypes

class CType(ctypes.Structure):
    pass

from .VkGeometryDataNV import CType as VkGeometryDataNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('geometryType', ctypes.c_int),
    ('geometry', VkGeometryDataNV),
    ('flags', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkGeometryDataNV',
    },
    'included_in': {
        'VkAccelerationStructureInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GEOMETRY_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'geometryType': {'python_name': ['geometry', 'type'], 'type': 'VkGeometryTypeKHR'},
        'geometry': {'python_name': ['geometry'], 'type': 'VkGeometryDataNV'},
        'flags': {'python_name': ['flags'], 'type': 'VkGeometryFlagsKHR'},
    }
}
