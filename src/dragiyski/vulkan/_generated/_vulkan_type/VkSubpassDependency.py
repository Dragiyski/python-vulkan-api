import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcSubpass', ctypes.c_uint32),
        ('dstSubpass', ctypes.c_uint32),
        ('srcStageMask', ctypes.c_uint32),
        ('dstStageMask', ctypes.c_uint32),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('dependencyFlags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRenderPassCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'srcSubpass': {'python_name': ['src', 'subpass']},
        'dstSubpass': {'python_name': ['dst', 'subpass']},
        'srcStageMask': {'python_name': ['src', 'stage', 'mask'], 'type': 'VkPipelineStageFlags'},
        'dstStageMask': {'python_name': ['dst', 'stage', 'mask'], 'type': 'VkPipelineStageFlags'},
        'srcAccessMask': {'python_name': ['src', 'access', 'mask'], 'type': 'VkAccessFlags'},
        'dstAccessMask': {'python_name': ['dst', 'access', 'mask'], 'type': 'VkAccessFlags'},
        'dependencyFlags': {'python_name': ['dependency', 'flags'], 'type': 'VkDependencyFlags'},
    }
}
