import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pName', ctypes.c_char_p),
        ('index', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPipelineShaderStageCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetExecutionGraphPipelineNodeIndexAMDX',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_NODE_CREATE_INFO_AMDX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pName': {'python_name': ['p', 'name'], 'len': [['null-terminated']]},
        'index': {'python_name': ['index']},
    }
}
