import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxExecutionGraphDepth', ctypes.c_uint32),
        ('maxExecutionGraphShaderOutputNodes', ctypes.c_uint32),
        ('maxExecutionGraphShaderPayloadSize', ctypes.c_uint32),
        ('maxExecutionGraphShaderPayloadCount', ctypes.c_uint32),
        ('executionGraphDispatchAddressAlignment', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ENQUEUE_PROPERTIES_AMDX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxExecutionGraphDepth': {'python_name': ['max', 'execution', 'graph', 'depth']},
        'maxExecutionGraphShaderOutputNodes': {'python_name': ['max', 'execution', 'graph', 'shader', 'output', 'nodes']},
        'maxExecutionGraphShaderPayloadSize': {'python_name': ['max', 'execution', 'graph', 'shader', 'payload', 'size']},
        'maxExecutionGraphShaderPayloadCount': {'python_name': ['max', 'execution', 'graph', 'shader', 'payload', 'count']},
        'executionGraphDispatchAddressAlignment': {'python_name': ['execution', 'graph', 'dispatch', 'address', 'alignment']},
    }
}
