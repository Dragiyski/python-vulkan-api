import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('resourceDeviceIndex', ctypes.c_uint32),
        ('memoryDeviceIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkBindSparseInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_BIND_SPARSE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'resourceDeviceIndex': {'python_name': ['resource', 'device', 'index']},
        'memoryDeviceIndex': {'python_name': ['memory', 'device', 'index']},
    }
}
