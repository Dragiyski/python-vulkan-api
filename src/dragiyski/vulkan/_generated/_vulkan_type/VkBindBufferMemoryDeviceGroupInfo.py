import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceIndexCount', ctypes.c_uint32),
        ('pDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkBindBufferMemoryInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_DEVICE_GROUP_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceIndexCount': {'python_name': ['device', 'index', 'count']},
        'pDeviceIndices': {'python_name': ['p', 'device', 'indices'], 'len': [['deviceIndexCount']]},
    }
}
