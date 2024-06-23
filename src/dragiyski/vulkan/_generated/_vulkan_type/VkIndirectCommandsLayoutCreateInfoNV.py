import ctypes

class CType(ctypes.Structure):
    pass

from .VkIndirectCommandsLayoutTokenNV import CType as VkIndirectCommandsLayoutTokenNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('tokenCount', ctypes.c_uint32),
    ('pTokens', ctypes.POINTER(VkIndirectCommandsLayoutTokenNV)),
    ('streamCount', ctypes.c_uint32),
    ('pStreamStrides', ctypes.POINTER(ctypes.c_uint32)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkIndirectCommandsLayoutTokenNV',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateIndirectCommandsLayoutNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkIndirectCommandsLayoutUsageFlagsNV'},
        'pipelineBindPoint': {'python_name': ['pipeline', 'bind', 'point'], 'type': 'VkPipelineBindPoint'},
        'tokenCount': {'python_name': ['token', 'count']},
        'pTokens': {'python_name': ['p', 'tokens'], 'len': [['tokenCount']], 'type': 'VkIndirectCommandsLayoutTokenNV'},
        'streamCount': {'python_name': ['stream', 'count']},
        'pStreamStrides': {'python_name': ['p', 'stream', 'strides'], 'len': [['streamCount']]},
    }
}
