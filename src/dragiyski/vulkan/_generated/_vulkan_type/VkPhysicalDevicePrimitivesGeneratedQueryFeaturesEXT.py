import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitivesGeneratedQuery', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithRasterizerDiscard', ctypes.c_uint32),
        ('primitivesGeneratedQueryWithNonZeroStreams', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PRIMITIVES_GENERATED_QUERY_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'primitivesGeneratedQuery': {'python_name': ['primitives', 'generated', 'query']},
        'primitivesGeneratedQueryWithRasterizerDiscard': {'python_name': ['primitives', 'generated', 'query', 'with', 'rasterizer', 'discard']},
        'primitivesGeneratedQueryWithNonZeroStreams': {'python_name': ['primitives', 'generated', 'query', 'with', 'non', 'zero', 'streams']},
    }
}
