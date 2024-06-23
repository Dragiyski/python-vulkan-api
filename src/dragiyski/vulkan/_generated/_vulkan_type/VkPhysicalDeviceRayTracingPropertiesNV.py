import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderGroupHandleSize', ctypes.c_uint32),
        ('maxRecursionDepth', ctypes.c_uint32),
        ('maxShaderGroupStride', ctypes.c_uint32),
        ('shaderGroupBaseAlignment', ctypes.c_uint32),
        ('maxGeometryCount', ctypes.c_uint64),
        ('maxInstanceCount', ctypes.c_uint64),
        ('maxTriangleCount', ctypes.c_uint64),
        ('maxDescriptorSetAccelerationStructures', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PROPERTIES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderGroupHandleSize': {'python_name': ['shader', 'group', 'handle', 'size']},
        'maxRecursionDepth': {'python_name': ['max', 'recursion', 'depth']},
        'maxShaderGroupStride': {'python_name': ['max', 'shader', 'group', 'stride']},
        'shaderGroupBaseAlignment': {'python_name': ['shader', 'group', 'base', 'alignment']},
        'maxGeometryCount': {'python_name': ['max', 'geometry', 'count']},
        'maxInstanceCount': {'python_name': ['max', 'instance', 'count']},
        'maxTriangleCount': {'python_name': ['max', 'triangle', 'count']},
        'maxDescriptorSetAccelerationStructures': {'python_name': ['max', 'descriptor', 'set', 'acceleration', 'structures']},
    }
}
