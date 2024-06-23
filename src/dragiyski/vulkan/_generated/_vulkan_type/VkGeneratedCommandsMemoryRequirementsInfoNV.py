import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineBindPoint', ctypes.c_int),
        ('pipeline', ctypes.c_void_p),
        ('indirectCommandsLayout', ctypes.c_void_p),
        ('maxSequencesCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetGeneratedCommandsMemoryRequirementsNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pipelineBindPoint': {'python_name': ['pipeline', 'bind', 'point'], 'type': 'VkPipelineBindPoint'},
        'pipeline': {'python_name': ['pipeline']},
        'indirectCommandsLayout': {'python_name': ['indirect', 'commands', 'layout']},
        'maxSequencesCount': {'python_name': ['max', 'sequences', 'count']},
    }
}
