import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stages', ctypes.c_uint32),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('subgroupSize', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPipelineExecutablePropertiesKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_EXECUTABLE_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stages': {'python_name': ['stages'], 'type': 'VkShaderStageFlags'},
        'name': {'python_name': ['name'], 'len': [['null-terminated']]},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
        'subgroupSize': {'python_name': ['subgroup', 'size']},
    }
}
