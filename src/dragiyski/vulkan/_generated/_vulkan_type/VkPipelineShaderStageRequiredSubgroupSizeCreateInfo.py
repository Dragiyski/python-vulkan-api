import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('requiredSubgroupSize', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPipelineShaderStageCreateInfo',
        'VkShaderCreateInfoEXT',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_REQUIRED_SUBGROUP_SIZE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'requiredSubgroupSize': {'python_name': ['required', 'subgroup', 'size']},
    }
}
