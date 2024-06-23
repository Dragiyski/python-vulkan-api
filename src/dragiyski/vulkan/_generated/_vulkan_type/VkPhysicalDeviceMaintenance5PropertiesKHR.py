import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('earlyFragmentMultisampleCoverageAfterSampleCounting', ctypes.c_uint32),
        ('earlyFragmentSampleMaskTestBeforeSampleCounting', ctypes.c_uint32),
        ('depthStencilSwizzleOneSupport', ctypes.c_uint32),
        ('polygonModePointSize', ctypes.c_uint32),
        ('nonStrictSinglePixelWideLinesUseParallelogram', ctypes.c_uint32),
        ('nonStrictWideLinesUseParallelogram', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_5_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'earlyFragmentMultisampleCoverageAfterSampleCounting': {'python_name': ['early', 'fragment', 'multisample', 'coverage', 'after', 'sample', 'counting']},
        'earlyFragmentSampleMaskTestBeforeSampleCounting': {'python_name': ['early', 'fragment', 'sample', 'mask', 'test', 'before', 'sample', 'counting']},
        'depthStencilSwizzleOneSupport': {'python_name': ['depth', 'stencil', 'swizzle', 'one', 'support']},
        'polygonModePointSize': {'python_name': ['polygon', 'mode', 'point', 'size']},
        'nonStrictSinglePixelWideLinesUseParallelogram': {'python_name': ['non', 'strict', 'single', 'pixel', 'wide', 'lines', 'use', 'parallelogram']},
        'nonStrictWideLinesUseParallelogram': {'python_name': ['non', 'strict', 'wide', 'lines', 'use', 'parallelogram']},
    }
}
