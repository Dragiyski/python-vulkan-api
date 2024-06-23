import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('flags', ctypes.c_uint32),
        ('duration', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineCreationFeedbackCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCreationFeedbackFlags'},
        'duration': {'python_name': ['duration']},
    }
}
