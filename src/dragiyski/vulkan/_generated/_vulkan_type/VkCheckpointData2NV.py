import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stage', ctypes.c_uint64),
        ('pCheckpointMarker', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetQueueCheckpointData2NV',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_CHECKPOINT_DATA_2_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stage': {'python_name': ['stage'], 'type': 'VkPipelineStageFlags2'},
        'pCheckpointMarker': {'python_name': ['p', 'checkpoint', 'marker']},
    }
}
