import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('constantAlphaColorBlendFactors', ctypes.c_uint32),
        ('events', ctypes.c_uint32),
        ('imageViewFormatReinterpretation', ctypes.c_uint32),
        ('imageViewFormatSwizzle', ctypes.c_uint32),
        ('imageView2DOn3DImage', ctypes.c_uint32),
        ('multisampleArrayImage', ctypes.c_uint32),
        ('mutableComparisonSamplers', ctypes.c_uint32),
        ('pointPolygons', ctypes.c_uint32),
        ('samplerMipLodBias', ctypes.c_uint32),
        ('separateStencilMaskRef', ctypes.c_uint32),
        ('shaderSampleRateInterpolationFunctions', ctypes.c_uint32),
        ('tessellationIsolines', ctypes.c_uint32),
        ('tessellationPointMode', ctypes.c_uint32),
        ('triangleFans', ctypes.c_uint32),
        ('vertexAttributeAccessBeyondStride', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PORTABILITY_SUBSET_FEATURES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'constantAlphaColorBlendFactors': {'python_name': ['constant', 'alpha', 'color', 'blend', 'factors']},
        'events': {'python_name': ['events']},
        'imageViewFormatReinterpretation': {'python_name': ['image', 'view', 'format', 'reinterpretation']},
        'imageViewFormatSwizzle': {'python_name': ['image', 'view', 'format', 'swizzle']},
        'imageView2DOn3DImage': {'python_name': ['image', 'view2', 'don3', 'dimage']},
        'multisampleArrayImage': {'python_name': ['multisample', 'array', 'image']},
        'mutableComparisonSamplers': {'python_name': ['mutable', 'comparison', 'samplers']},
        'pointPolygons': {'python_name': ['point', 'polygons']},
        'samplerMipLodBias': {'python_name': ['sampler', 'mip', 'lod', 'bias']},
        'separateStencilMaskRef': {'python_name': ['separate', 'stencil', 'mask', 'ref']},
        'shaderSampleRateInterpolationFunctions': {'python_name': ['shader', 'sample', 'rate', 'interpolation', 'functions']},
        'tessellationIsolines': {'python_name': ['tessellation', 'isolines']},
        'tessellationPointMode': {'python_name': ['tessellation', 'point', 'mode']},
        'triangleFans': {'python_name': ['triangle', 'fans']},
        'vertexAttributeAccessBeyondStride': {'python_name': ['vertex', 'attribute', 'access', 'beyond', 'stride']},
    }
}
