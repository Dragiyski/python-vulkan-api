import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('bufferView', ctypes.c_void_p),
        ('plane', ctypes.c_uint32),
        ('mtlTexture', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkExportMetalObjectsInfoEXT',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXPORT_METAL_TEXTURE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'image': {'python_name': ['image']},
        'imageView': {'python_name': ['image', 'view']},
        'bufferView': {'python_name': ['buffer', 'view']},
        'plane': {'python_name': ['plane'], 'type': 'VkImageAspectFlagBits'},
        'mtlTexture': {'python_name': ['mtl', 'texture']},
    }
}
