import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderBufferFloat16Atomics', ctypes.c_uint32),
        ('shaderBufferFloat16AtomicAdd', ctypes.c_uint32),
        ('shaderBufferFloat16AtomicMinMax', ctypes.c_uint32),
        ('shaderBufferFloat32AtomicMinMax', ctypes.c_uint32),
        ('shaderBufferFloat64AtomicMinMax', ctypes.c_uint32),
        ('shaderSharedFloat16Atomics', ctypes.c_uint32),
        ('shaderSharedFloat16AtomicAdd', ctypes.c_uint32),
        ('shaderSharedFloat16AtomicMinMax', ctypes.c_uint32),
        ('shaderSharedFloat32AtomicMinMax', ctypes.c_uint32),
        ('shaderSharedFloat64AtomicMinMax', ctypes.c_uint32),
        ('shaderImageFloat32AtomicMinMax', ctypes.c_uint32),
        ('sparseImageFloat32AtomicMinMax', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_2_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderBufferFloat16Atomics': {'python_name': ['shader', 'buffer', 'float16', 'atomics']},
        'shaderBufferFloat16AtomicAdd': {'python_name': ['shader', 'buffer', 'float16', 'atomic', 'add']},
        'shaderBufferFloat16AtomicMinMax': {'python_name': ['shader', 'buffer', 'float16', 'atomic', 'min', 'max']},
        'shaderBufferFloat32AtomicMinMax': {'python_name': ['shader', 'buffer', 'float32', 'atomic', 'min', 'max']},
        'shaderBufferFloat64AtomicMinMax': {'python_name': ['shader', 'buffer', 'float64', 'atomic', 'min', 'max']},
        'shaderSharedFloat16Atomics': {'python_name': ['shader', 'shared', 'float16', 'atomics']},
        'shaderSharedFloat16AtomicAdd': {'python_name': ['shader', 'shared', 'float16', 'atomic', 'add']},
        'shaderSharedFloat16AtomicMinMax': {'python_name': ['shader', 'shared', 'float16', 'atomic', 'min', 'max']},
        'shaderSharedFloat32AtomicMinMax': {'python_name': ['shader', 'shared', 'float32', 'atomic', 'min', 'max']},
        'shaderSharedFloat64AtomicMinMax': {'python_name': ['shader', 'shared', 'float64', 'atomic', 'min', 'max']},
        'shaderImageFloat32AtomicMinMax': {'python_name': ['shader', 'image', 'float32', 'atomic', 'min', 'max']},
        'sparseImageFloat32AtomicMinMax': {'python_name': ['sparse', 'image', 'float32', 'atomic', 'min', 'max']},
    }
}
