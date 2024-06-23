import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('initialDataSize', ctypes.c_size_t),
        ('pInitialData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDeviceObjectReservationCreateInfo',
    },
    'input_of': {
        'vkCreatePipelineCache',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_CACHE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCacheCreateFlags'},
        'initialDataSize': {'python_name': ['initial', 'data', 'size']},
        'pInitialData': {'python_name': ['p', 'initial', 'data'], 'len': [['initialDataSize']]},
    }
}
