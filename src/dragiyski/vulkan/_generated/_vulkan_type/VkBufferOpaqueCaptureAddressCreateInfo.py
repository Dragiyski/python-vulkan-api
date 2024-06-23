import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('opaqueCaptureAddress', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkBufferCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_OPAQUE_CAPTURE_ADDRESS_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'opaqueCaptureAddress': {'python_name': ['opaque', 'capture', 'address']},
    }
}
