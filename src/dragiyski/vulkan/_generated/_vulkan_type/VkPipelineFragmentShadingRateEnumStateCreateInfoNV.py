import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shadingRateType', ctypes.c_int),
        ('shadingRate', ctypes.c_int),
        ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
    ]

descriptor = {
    'extends': {
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_FRAGMENT_SHADING_RATE_ENUM_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shadingRateType': {'python_name': ['shading', 'rate', 'type'], 'type': 'VkFragmentShadingRateTypeNV'},
        'shadingRate': {'python_name': ['shading', 'rate'], 'type': 'VkFragmentShadingRateNV'},
        'combinerOps': {'python_name': ['combiner', 'ops'], 'type': 'VkFragmentShadingRateCombinerOpKHR'},
    }
}
