import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('decodeMode', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkImageViewCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_ASTC_DECODE_MODE_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'decodeMode': {'python_name': ['decode', 'mode'], 'type': 'VkFormat'},
    }
}
