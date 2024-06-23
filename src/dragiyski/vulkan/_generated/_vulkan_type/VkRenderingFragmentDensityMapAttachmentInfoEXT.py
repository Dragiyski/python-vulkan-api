import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('imageLayout', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkRenderingInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDERING_FRAGMENT_DENSITY_MAP_ATTACHMENT_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageView': {'python_name': ['image', 'view']},
        'imageLayout': {'python_name': ['image', 'layout'], 'type': 'VkImageLayout'},
    }
}
