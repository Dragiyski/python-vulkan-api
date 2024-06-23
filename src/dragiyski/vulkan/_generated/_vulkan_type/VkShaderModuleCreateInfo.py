import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('codeSize', ctypes.c_size_t),
        ('pCode', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkPipelineShaderStageCreateInfo',
    },
    'extended_by': {
        'VkShaderModuleValidationCacheCreateInfoEXT',
        'VkValidationFeaturesEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateShaderModule',
        'vkGetShaderModuleCreateInfoIdentifierEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkShaderModuleCreateFlags'},
        'codeSize': {'python_name': ['code', 'size']},
        'pCode': {'python_name': ['p', 'code'], 'len': [['latexmath:[\\textrm{codeSize} \\over 4]']]},
    }
}
