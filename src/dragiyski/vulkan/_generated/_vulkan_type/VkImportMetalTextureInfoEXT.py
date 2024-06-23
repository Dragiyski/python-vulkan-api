import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('plane', ctypes.c_uint32),
        ('mtlTexture', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMPORT_METAL_TEXTURE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'plane': {'python_name': ['plane'], 'type': 'VkImageAspectFlagBits'},
        'mtlTexture': {'python_name': ['mtl', 'texture']},
    }
}
