import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcStageMask', ctypes.c_uint64),
        ('srcAccessMask', ctypes.c_uint64),
        ('dstStageMask', ctypes.c_uint64),
        ('dstAccessMask', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkSubpassDependency2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDependencyInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MEMORY_BARRIER_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcStageMask': {'python_name': ['src', 'stage', 'mask'], 'type': 'VkPipelineStageFlags2'},
        'srcAccessMask': {'python_name': ['src', 'access', 'mask'], 'type': 'VkAccessFlags2'},
        'dstStageMask': {'python_name': ['dst', 'stage', 'mask'], 'type': 'VkPipelineStageFlags2'},
        'dstAccessMask': {'python_name': ['dst', 'access', 'mask'], 'type': 'VkAccessFlags2'},
    }
}
