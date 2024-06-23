import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vendorID', ctypes.c_uint32),
        ('deviceID', ctypes.c_uint32),
        ('key', ctypes.c_uint32),
        ('value', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkApplicationInfo',
        'VkDeviceCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_APPLICATION_PARAMETERS_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'vendorID': {'python_name': ['vendor', 'id']},
        'deviceID': {'python_name': ['device', 'id']},
        'key': {'python_name': ['key']},
        'value': {'python_name': ['value']},
    }
}
