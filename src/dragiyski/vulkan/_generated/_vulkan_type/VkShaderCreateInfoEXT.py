import ctypes

class CType(ctypes.Structure):
    pass

from .VkPushConstantRange import CType as VkPushConstantRange
from .VkSpecializationInfo import CType as VkSpecializationInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', ctypes.c_uint32),
    ('nextStage', ctypes.c_uint32),
    ('codeType', ctypes.c_int),
    ('codeSize', ctypes.c_size_t),
    ('pCode', ctypes.c_void_p),
    ('pName', ctypes.c_char_p),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
    ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineShaderStageRequiredSubgroupSizeCreateInfo',
        'VkValidationFeaturesEXT',
    },
    'includes': {
        'VkPushConstantRange',
        'VkSpecializationInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateShadersEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SHADER_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkShaderCreateFlagsEXT'},
        'stage': {'python_name': ['stage'], 'type': 'VkShaderStageFlagBits'},
        'nextStage': {'python_name': ['next', 'stage'], 'type': 'VkShaderStageFlags'},
        'codeType': {'python_name': ['code', 'type'], 'type': 'VkShaderCodeTypeEXT'},
        'codeSize': {'python_name': ['code', 'size']},
        'pCode': {'python_name': ['p', 'code'], 'len': [['codeSize']]},
        'pName': {'python_name': ['p', 'name'], 'len': [['null-terminated']]},
        'setLayoutCount': {'python_name': ['set', 'layout', 'count']},
        'pSetLayouts': {'python_name': ['p', 'set', 'layouts'], 'len': [['setLayoutCount']]},
        'pushConstantRangeCount': {'python_name': ['push', 'constant', 'range', 'count']},
        'pPushConstantRanges': {'python_name': ['p', 'push', 'constant', 'ranges'], 'len': [['pushConstantRangeCount']], 'type': 'VkPushConstantRange'},
        'pSpecializationInfo': {'python_name': ['p', 'specialization', 'info'], 'type': 'VkSpecializationInfo'},
    }
}
