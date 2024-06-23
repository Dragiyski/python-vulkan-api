import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportedDepthResolveModes', ctypes.c_uint32),
        ('supportedStencilResolveModes', ctypes.c_uint32),
        ('independentResolveNone', ctypes.c_uint32),
        ('independentResolve', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_STENCIL_RESOLVE_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'supportedDepthResolveModes': {'python_name': ['supported', 'depth', 'resolve', 'modes'], 'type': 'VkResolveModeFlags'},
        'supportedStencilResolveModes': {'python_name': ['supported', 'stencil', 'resolve', 'modes'], 'type': 'VkResolveModeFlags'},
        'independentResolveNone': {'python_name': ['independent', 'resolve', 'none']},
        'independentResolve': {'python_name': ['independent', 'resolve']},
    }
}
