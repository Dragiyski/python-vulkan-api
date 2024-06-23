import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingMotionBlur', ctypes.c_uint32),
        ('rayTracingMotionBlurPipelineTraceRaysIndirect', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_MOTION_BLUR_FEATURES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'rayTracingMotionBlur': {'python_name': ['ray', 'tracing', 'motion', 'blur']},
        'rayTracingMotionBlurPipelineTraceRaysIndirect': {'python_name': ['ray', 'tracing', 'motion', 'blur', 'pipeline', 'trace', 'rays', 'indirect']},
    }
}
