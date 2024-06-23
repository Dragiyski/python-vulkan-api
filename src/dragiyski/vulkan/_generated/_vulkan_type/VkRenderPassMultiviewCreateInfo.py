import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subpassCount', ctypes.c_uint32),
        ('pViewMasks', ctypes.POINTER(ctypes.c_uint32)),
        ('dependencyCount', ctypes.c_uint32),
        ('pViewOffsets', ctypes.POINTER(ctypes.c_int32)),
        ('correlationMaskCount', ctypes.c_uint32),
        ('pCorrelationMasks', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkRenderPassCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_MULTIVIEW_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'subpassCount': {'python_name': ['subpass', 'count']},
        'pViewMasks': {'python_name': ['p', 'view', 'masks'], 'len': [['subpassCount']]},
        'dependencyCount': {'python_name': ['dependency', 'count']},
        'pViewOffsets': {'python_name': ['p', 'view', 'offsets'], 'len': [['dependencyCount']]},
        'correlationMaskCount': {'python_name': ['correlation', 'mask', 'count']},
        'pCorrelationMasks': {'python_name': ['p', 'correlation', 'masks'], 'len': [['correlationMaskCount']]},
    }
}
