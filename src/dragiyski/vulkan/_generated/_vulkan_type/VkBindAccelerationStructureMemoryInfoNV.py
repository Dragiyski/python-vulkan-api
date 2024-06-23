import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('accelerationStructure', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('deviceIndexCount', ctypes.c_uint32),
        ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkBindAccelerationStructureMemoryNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_ACCELERATION_STRUCTURE_MEMORY_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'accelerationStructure': {'python_name': ['acceleration', 'structure']},
        'memory': {'python_name': ['memory']},
        'memoryOffset': {'python_name': ['memory', 'offset']},
        'deviceIndexCount': {'python_name': ['device', 'index', 'count']},
        'pDeviceIndices': {'python_name': ['p', 'device', 'indices'], 'len': [['deviceIndexCount']]},
    }
}
