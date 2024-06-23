import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingMaintenance1', ctypes.c_uint32),
        ('rayTracingPipelineTraceRaysIndirect2', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_MAINTENANCE_1_FEATURES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'rayTracingMaintenance1': {'python_name': ['ray', 'tracing', 'maintenance1']},
        'rayTracingPipelineTraceRaysIndirect2': {'python_name': ['ray', 'tracing', 'pipeline', 'trace', 'rays', 'indirect2']},
    }
}
