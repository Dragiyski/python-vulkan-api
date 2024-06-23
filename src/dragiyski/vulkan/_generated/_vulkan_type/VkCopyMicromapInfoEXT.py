import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('src', ctypes.c_void_p),
        ('dst', ctypes.c_void_p),
        ('mode', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdCopyMicromapEXT',
        'vkCopyMicromapEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_MICROMAP_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'src': {'python_name': ['src']},
        'dst': {'python_name': ['dst']},
        'mode': {'python_name': ['mode'], 'type': 'VkCopyMicromapModeEXT'},
    }
}
