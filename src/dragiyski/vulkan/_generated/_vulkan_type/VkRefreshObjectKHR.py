import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRefreshObjectListKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'objectType': {'python_name': ['object', 'type'], 'type': 'VkObjectType'},
        'objectHandle': {'python_name': ['object', 'handle'], 'externsync': [['true']]},
        'flags': {'python_name': ['flags'], 'type': 'VkRefreshObjectFlagsKHR'},
    }
}
