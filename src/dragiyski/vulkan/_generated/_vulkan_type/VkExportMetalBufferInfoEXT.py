import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('mtlBuffer', ctypes.c_void_p),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXPORT_METAL_BUFFER_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memory': {'python_name': ['memory']},
        'mtlBuffer': {'python_name': ['mtl', 'buffer']},
    }
}
