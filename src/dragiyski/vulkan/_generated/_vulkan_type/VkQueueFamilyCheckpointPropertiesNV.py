import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('checkpointExecutionStageMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkQueueFamilyProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_CHECKPOINT_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'checkpointExecutionStageMask': {'python_name': ['checkpoint', 'execution', 'stage', 'mask'], 'type': 'VkPipelineStageFlags'},
    }
}
