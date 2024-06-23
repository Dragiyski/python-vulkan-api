import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lineRasterizationMode', ctypes.c_int),
        ('stippledLineEnable', ctypes.c_uint32),
        ('lineStippleFactor', ctypes.c_uint32),
        ('lineStipplePattern', ctypes.c_uint16),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_LINE_STATE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'lineRasterizationMode': {'python_name': ['line', 'rasterization', 'mode'], 'type': 'VkLineRasterizationModeKHR'},
        'stippledLineEnable': {'python_name': ['stippled', 'line', 'enable']},
        'lineStippleFactor': {'python_name': ['line', 'stipple', 'factor']},
        'lineStipplePattern': {'python_name': ['line', 'stipple', 'pattern']},
    }
}
