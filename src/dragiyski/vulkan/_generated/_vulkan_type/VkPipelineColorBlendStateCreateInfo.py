import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineColorBlendAttachmentState import CType as VkPipelineColorBlendAttachmentState

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('logicOpEnable', ctypes.c_uint32),
    ('logicOp', ctypes.c_int),
    ('attachmentCount', ctypes.c_uint32),
    ('pAttachments', ctypes.POINTER(VkPipelineColorBlendAttachmentState)),
    ('blendConstants', ctypes.ARRAY(ctypes.c_float, 4)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineColorBlendAdvancedStateCreateInfoEXT',
        'VkPipelineColorWriteCreateInfoEXT',
    },
    'includes': {
        'VkPipelineColorBlendAttachmentState',
    },
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineColorBlendStateCreateFlags'},
        'logicOpEnable': {'python_name': ['logic', 'op', 'enable']},
        'logicOp': {'python_name': ['logic', 'op'], 'type': 'VkLogicOp'},
        'attachmentCount': {'python_name': ['attachment', 'count']},
        'pAttachments': {'python_name': ['p', 'attachments'], 'len': [['attachmentCount']], 'type': 'VkPipelineColorBlendAttachmentState'},
        'blendConstants': {'python_name': ['blend', 'constants']},
    }
}
