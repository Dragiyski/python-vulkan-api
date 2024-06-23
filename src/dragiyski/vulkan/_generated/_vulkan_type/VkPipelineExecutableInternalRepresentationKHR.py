import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('isText', ctypes.c_uint32),
        ('dataSize', ctypes.c_size_t),
        ('pData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPipelineExecutableInternalRepresentationsKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_INTERNAL_REPRESENTATION_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'name': {'python_name': ['name'], 'len': [['null-terminated']]},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
        'isText': {'python_name': ['is', 'text']},
        'dataSize': {'python_name': ['data', 'size']},
        'pData': {'python_name': ['p', 'data'], 'len': [['dataSize']]},
    }
}
