import ctypes

class CType(ctypes.Structure):
    pass

from .VkIndirectCommandsStreamNV import CType as VkIndirectCommandsStreamNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pipelineBindPoint', ctypes.c_int),
    ('pipeline', ctypes.c_void_p),
    ('indirectCommandsLayout', ctypes.c_void_p),
    ('streamCount', ctypes.c_uint32),
    ('pStreams', ctypes.POINTER(VkIndirectCommandsStreamNV)),
    ('sequencesCount', ctypes.c_uint32),
    ('preprocessBuffer', ctypes.c_void_p),
    ('preprocessOffset', ctypes.c_uint64),
    ('preprocessSize', ctypes.c_uint64),
    ('sequencesCountBuffer', ctypes.c_void_p),
    ('sequencesCountOffset', ctypes.c_uint64),
    ('sequencesIndexBuffer', ctypes.c_void_p),
    ('sequencesIndexOffset', ctypes.c_uint64),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkIndirectCommandsStreamNV',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdExecuteGeneratedCommandsNV',
        'vkCmdPreprocessGeneratedCommandsNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pipelineBindPoint': {'python_name': ['pipeline', 'bind', 'point'], 'type': 'VkPipelineBindPoint'},
        'pipeline': {'python_name': ['pipeline']},
        'indirectCommandsLayout': {'python_name': ['indirect', 'commands', 'layout']},
        'streamCount': {'python_name': ['stream', 'count']},
        'pStreams': {'python_name': ['p', 'streams'], 'len': [['streamCount']], 'type': 'VkIndirectCommandsStreamNV'},
        'sequencesCount': {'python_name': ['sequences', 'count']},
        'preprocessBuffer': {'python_name': ['preprocess', 'buffer']},
        'preprocessOffset': {'python_name': ['preprocess', 'offset']},
        'preprocessSize': {'python_name': ['preprocess', 'size']},
        'sequencesCountBuffer': {'python_name': ['sequences', 'count', 'buffer']},
        'sequencesCountOffset': {'python_name': ['sequences', 'count', 'offset']},
        'sequencesIndexBuffer': {'python_name': ['sequences', 'index', 'buffer']},
        'sequencesIndexOffset': {'python_name': ['sequences', 'index', 'offset']},
    }
}
