import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pAttributes', ctypes.c_void_p),
        ('dwAccess', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkMemoryAllocateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pAttributes': {'python_name': ['p', 'attributes']},
        'dwAccess': {'python_name': ['dw', 'access']},
    }
}
