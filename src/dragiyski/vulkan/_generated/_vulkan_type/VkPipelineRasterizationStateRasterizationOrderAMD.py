import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rasterizationOrder', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkPipelineRasterizationStateCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_RASTERIZATION_ORDER_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'rasterizationOrder': {'python_name': ['rasterization', 'order'], 'type': 'VkRasterizationOrderAMD'},
    }
}
