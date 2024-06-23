import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcSubpass', ctypes.c_uint32),
        ('dstSubpass', ctypes.c_uint32),
        ('srcStageMask', ctypes.c_uint32),
        ('dstStageMask', ctypes.c_uint32),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('dependencyFlags', ctypes.c_uint32),
        ('viewOffset', ctypes.c_int32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkMemoryBarrier2',
    },
    'includes': set(),
    'included_in': {
        'VkRenderPassCreateInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_DEPENDENCY_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcSubpass': {'python_name': ['src', 'subpass']},
        'dstSubpass': {'python_name': ['dst', 'subpass']},
        'srcStageMask': {'python_name': ['src', 'stage', 'mask'], 'type': 'VkPipelineStageFlags'},
        'dstStageMask': {'python_name': ['dst', 'stage', 'mask'], 'type': 'VkPipelineStageFlags'},
        'srcAccessMask': {'python_name': ['src', 'access', 'mask'], 'type': 'VkAccessFlags'},
        'dstAccessMask': {'python_name': ['dst', 'access', 'mask'], 'type': 'VkAccessFlags'},
        'dependencyFlags': {'python_name': ['dependency', 'flags'], 'type': 'VkDependencyFlags'},
        'viewOffset': {'python_name': ['view', 'offset']},
    }
}
