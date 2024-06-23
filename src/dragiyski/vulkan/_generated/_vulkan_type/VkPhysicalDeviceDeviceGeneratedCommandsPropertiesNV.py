import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxGraphicsShaderGroupCount', ctypes.c_uint32),
        ('maxIndirectSequenceCount', ctypes.c_uint32),
        ('maxIndirectCommandsTokenCount', ctypes.c_uint32),
        ('maxIndirectCommandsStreamCount', ctypes.c_uint32),
        ('maxIndirectCommandsTokenOffset', ctypes.c_uint32),
        ('maxIndirectCommandsStreamStride', ctypes.c_uint32),
        ('minSequencesCountBufferOffsetAlignment', ctypes.c_uint32),
        ('minSequencesIndexBufferOffsetAlignment', ctypes.c_uint32),
        ('minIndirectCommandsBufferOffsetAlignment', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxGraphicsShaderGroupCount': {'python_name': ['max', 'graphics', 'shader', 'group', 'count']},
        'maxIndirectSequenceCount': {'python_name': ['max', 'indirect', 'sequence', 'count']},
        'maxIndirectCommandsTokenCount': {'python_name': ['max', 'indirect', 'commands', 'token', 'count']},
        'maxIndirectCommandsStreamCount': {'python_name': ['max', 'indirect', 'commands', 'stream', 'count']},
        'maxIndirectCommandsTokenOffset': {'python_name': ['max', 'indirect', 'commands', 'token', 'offset']},
        'maxIndirectCommandsStreamStride': {'python_name': ['max', 'indirect', 'commands', 'stream', 'stride']},
        'minSequencesCountBufferOffsetAlignment': {'python_name': ['min', 'sequences', 'count', 'buffer', 'offset', 'alignment']},
        'minSequencesIndexBufferOffsetAlignment': {'python_name': ['min', 'sequences', 'index', 'buffer', 'offset', 'alignment']},
        'minIndirectCommandsBufferOffsetAlignment': {'python_name': ['min', 'indirect', 'commands', 'buffer', 'offset', 'alignment']},
    }
}
