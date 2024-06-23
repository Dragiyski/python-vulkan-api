import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('primitiveOverestimationSize', ctypes.c_float),
        ('maxExtraPrimitiveOverestimationSize', ctypes.c_float),
        ('extraPrimitiveOverestimationSizeGranularity', ctypes.c_float),
        ('primitiveUnderestimation', ctypes.c_uint32),
        ('conservativePointAndLineRasterization', ctypes.c_uint32),
        ('degenerateTrianglesRasterized', ctypes.c_uint32),
        ('degenerateLinesRasterized', ctypes.c_uint32),
        ('fullyCoveredFragmentShaderInputVariable', ctypes.c_uint32),
        ('conservativeRasterizationPostDepthCoverage', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_CONSERVATIVE_RASTERIZATION_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'primitiveOverestimationSize': {'python_name': ['primitive', 'overestimation', 'size']},
        'maxExtraPrimitiveOverestimationSize': {'python_name': ['max', 'extra', 'primitive', 'overestimation', 'size']},
        'extraPrimitiveOverestimationSizeGranularity': {'python_name': ['extra', 'primitive', 'overestimation', 'size', 'granularity']},
        'primitiveUnderestimation': {'python_name': ['primitive', 'underestimation']},
        'conservativePointAndLineRasterization': {'python_name': ['conservative', 'point', 'and', 'line', 'rasterization']},
        'degenerateTrianglesRasterized': {'python_name': ['degenerate', 'triangles', 'rasterized']},
        'degenerateLinesRasterized': {'python_name': ['degenerate', 'lines', 'rasterized']},
        'fullyCoveredFragmentShaderInputVariable': {'python_name': ['fully', 'covered', 'fragment', 'shader', 'input', 'variable']},
        'conservativeRasterizationPostDepthCoverage': {'python_name': ['conservative', 'rasterization', 'post', 'depth', 'coverage']},
    }
}
