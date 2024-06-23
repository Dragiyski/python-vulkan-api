import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('poolEntrySize', ctypes.c_uint64),
        ('poolEntryCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDeviceObjectReservationCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_POOL_SIZE', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'poolEntrySize': {'python_name': ['pool', 'entry', 'size']},
        'poolEntryCount': {'python_name': ['pool', 'entry', 'count']},
    }
}
