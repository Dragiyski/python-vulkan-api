import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('aabbData', ctypes.c_void_p),
        ('numAABBs', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('offset', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkGeometryDataNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GEOMETRY_AABB_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'aabbData': {'python_name': ['aabb', 'data']},
        'numAABBs': {'python_name': ['num', 'aabbs']},
        'stride': {'python_name': ['stride']},
        'offset': {'python_name': ['offset']},
    }
}
