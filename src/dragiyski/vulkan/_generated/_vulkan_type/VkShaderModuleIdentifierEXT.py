import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('identifier', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetShaderModuleCreateInfoIdentifierEXT',
        'vkGetShaderModuleIdentifierEXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SHADER_MODULE_IDENTIFIER_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'identifierSize': {'python_name': ['identifier', 'size']},
        'identifier': {'python_name': ['identifier'], 'len': [['identifierSize']]},
    }
}
