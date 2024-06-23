import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPipelineRayPayloadSize', ctypes.c_uint32),
        ('maxPipelineRayHitAttributeSize', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRayTracingPipelineCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_INTERFACE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxPipelineRayPayloadSize': {'python_name': ['max', 'pipeline', 'ray', 'payload', 'size']},
        'maxPipelineRayHitAttributeSize': {'python_name': ['max', 'pipeline', 'ray', 'hit', 'attribute', 'size']},
    }
}
