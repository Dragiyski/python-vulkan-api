import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetBufferDeviceAddress',
        'vkGetBufferOpaqueCaptureAddress',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_DEVICE_ADDRESS_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'buffer': {'python_name': ['buffer']},
    }
}
