import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('layout', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('pValues', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineLayoutCreateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdPushConstants2KHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PUSH_CONSTANTS_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'layout': {'python_name': ['layout']},
        'stageFlags': {'python_name': ['stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
        'pValues': {'python_name': ['p', 'values'], 'len': [['size']]},
    }
}
