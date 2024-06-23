import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('pIdentifier', ctypes.POINTER(ctypes.c_uint8)),
    ]

descriptor = {
    'extends': {
        'VkPipelineShaderStageCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_MODULE_IDENTIFIER_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'identifierSize': {'python_name': ['identifier', 'size']},
        'pIdentifier': {'python_name': ['p', 'identifier'], 'len': [['identifierSize']]},
    }
}
