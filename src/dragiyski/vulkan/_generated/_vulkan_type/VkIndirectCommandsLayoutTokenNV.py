import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('tokenType', ctypes.c_int),
        ('stream', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('vertexBindingUnit', ctypes.c_uint32),
        ('vertexDynamicStride', ctypes.c_uint32),
        ('pushconstantPipelineLayout', ctypes.c_void_p),
        ('pushconstantShaderStageFlags', ctypes.c_uint32),
        ('pushconstantOffset', ctypes.c_uint32),
        ('pushconstantSize', ctypes.c_uint32),
        ('indirectStateFlags', ctypes.c_uint32),
        ('indexTypeCount', ctypes.c_uint32),
        ('pIndexTypes', ctypes.POINTER(ctypes.c_int)),
        ('pIndexTypeValues', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkIndirectCommandsLayoutCreateInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'tokenType': {'python_name': ['token', 'type'], 'type': 'VkIndirectCommandsTokenTypeNV'},
        'stream': {'python_name': ['stream']},
        'offset': {'python_name': ['offset']},
        'vertexBindingUnit': {'python_name': ['vertex', 'binding', 'unit']},
        'vertexDynamicStride': {'python_name': ['vertex', 'dynamic', 'stride']},
        'pushconstantPipelineLayout': {'python_name': ['pushconstant', 'pipeline', 'layout']},
        'pushconstantShaderStageFlags': {'python_name': ['pushconstant', 'shader', 'stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'pushconstantOffset': {'python_name': ['pushconstant', 'offset']},
        'pushconstantSize': {'python_name': ['pushconstant', 'size']},
        'indirectStateFlags': {'python_name': ['indirect', 'state', 'flags'], 'type': 'VkIndirectStateFlagsNV'},
        'indexTypeCount': {'python_name': ['index', 'type', 'count']},
        'pIndexTypes': {'python_name': ['p', 'index', 'types'], 'len': [['indexTypeCount']], 'type': 'VkIndexType'},
        'pIndexTypeValues': {'python_name': ['p', 'index', 'type', 'values'], 'len': [['indexTypeCount']]},
    }
}
