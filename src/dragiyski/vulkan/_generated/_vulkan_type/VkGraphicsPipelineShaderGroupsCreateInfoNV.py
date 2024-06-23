import ctypes

class CType(ctypes.Structure):
    pass

from .VkGraphicsShaderGroupCreateInfoNV import CType as VkGraphicsShaderGroupCreateInfoNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV)),
    ('pipelineCount', ctypes.c_uint32),
    ('pPipelines', ctypes.POINTER(ctypes.c_void_p)),
]

descriptor = {
    'extends': {
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkGraphicsShaderGroupCreateInfoNV',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_SHADER_GROUPS_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'groupCount': {'python_name': ['group', 'count']},
        'pGroups': {'python_name': ['p', 'groups'], 'len': [['groupCount']], 'type': 'VkGraphicsShaderGroupCreateInfoNV'},
        'pipelineCount': {'python_name': ['pipeline', 'count']},
        'pPipelines': {'python_name': ['p', 'pipelines'], 'len': [['pipelineCount']]},
    }
}
