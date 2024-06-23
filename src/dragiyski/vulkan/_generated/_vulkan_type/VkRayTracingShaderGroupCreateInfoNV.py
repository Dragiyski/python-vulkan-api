import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
        ('generalShader', ctypes.c_uint32),
        ('closestHitShader', ctypes.c_uint32),
        ('anyHitShader', ctypes.c_uint32),
        ('intersectionShader', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRayTracingPipelineCreateInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_SHADER_GROUP_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'type': {'python_name': ['type'], 'type': 'VkRayTracingShaderGroupTypeKHR'},
        'generalShader': {'python_name': ['general', 'shader']},
        'closestHitShader': {'python_name': ['closest', 'hit', 'shader']},
        'anyHitShader': {'python_name': ['any', 'hit', 'shader']},
        'intersectionShader': {'python_name': ['intersection', 'shader']},
    }
}
