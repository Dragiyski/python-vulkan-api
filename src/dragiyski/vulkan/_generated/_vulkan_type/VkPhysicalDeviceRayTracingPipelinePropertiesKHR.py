import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderGroupHandleSize', ctypes.c_uint32),
        ('maxRayRecursionDepth', ctypes.c_uint32),
        ('maxShaderGroupStride', ctypes.c_uint32),
        ('shaderGroupBaseAlignment', ctypes.c_uint32),
        ('shaderGroupHandleCaptureReplaySize', ctypes.c_uint32),
        ('maxRayDispatchInvocationCount', ctypes.c_uint32),
        ('shaderGroupHandleAlignment', ctypes.c_uint32),
        ('maxRayHitAttributeSize', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderGroupHandleSize': {'python_name': ['shader', 'group', 'handle', 'size']},
        'maxRayRecursionDepth': {'python_name': ['max', 'ray', 'recursion', 'depth']},
        'maxShaderGroupStride': {'python_name': ['max', 'shader', 'group', 'stride']},
        'shaderGroupBaseAlignment': {'python_name': ['shader', 'group', 'base', 'alignment']},
        'shaderGroupHandleCaptureReplaySize': {'python_name': ['shader', 'group', 'handle', 'capture', 'replay', 'size']},
        'maxRayDispatchInvocationCount': {'python_name': ['max', 'ray', 'dispatch', 'invocation', 'count']},
        'shaderGroupHandleAlignment': {'python_name': ['shader', 'group', 'handle', 'alignment']},
        'maxRayHitAttributeSize': {'python_name': ['max', 'ray', 'hit', 'attribute', 'size']},
    }
}
