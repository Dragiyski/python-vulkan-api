import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderBufferFloat32Atomics', ctypes.c_uint32),
        ('shaderBufferFloat32AtomicAdd', ctypes.c_uint32),
        ('shaderBufferFloat64Atomics', ctypes.c_uint32),
        ('shaderBufferFloat64AtomicAdd', ctypes.c_uint32),
        ('shaderSharedFloat32Atomics', ctypes.c_uint32),
        ('shaderSharedFloat32AtomicAdd', ctypes.c_uint32),
        ('shaderSharedFloat64Atomics', ctypes.c_uint32),
        ('shaderSharedFloat64AtomicAdd', ctypes.c_uint32),
        ('shaderImageFloat32Atomics', ctypes.c_uint32),
        ('shaderImageFloat32AtomicAdd', ctypes.c_uint32),
        ('sparseImageFloat32Atomics', ctypes.c_uint32),
        ('sparseImageFloat32AtomicAdd', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_ATOMIC_FLOAT_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderBufferFloat32Atomics': {'python_name': ['shader', 'buffer', 'float32', 'atomics']},
        'shaderBufferFloat32AtomicAdd': {'python_name': ['shader', 'buffer', 'float32', 'atomic', 'add']},
        'shaderBufferFloat64Atomics': {'python_name': ['shader', 'buffer', 'float64', 'atomics']},
        'shaderBufferFloat64AtomicAdd': {'python_name': ['shader', 'buffer', 'float64', 'atomic', 'add']},
        'shaderSharedFloat32Atomics': {'python_name': ['shader', 'shared', 'float32', 'atomics']},
        'shaderSharedFloat32AtomicAdd': {'python_name': ['shader', 'shared', 'float32', 'atomic', 'add']},
        'shaderSharedFloat64Atomics': {'python_name': ['shader', 'shared', 'float64', 'atomics']},
        'shaderSharedFloat64AtomicAdd': {'python_name': ['shader', 'shared', 'float64', 'atomic', 'add']},
        'shaderImageFloat32Atomics': {'python_name': ['shader', 'image', 'float32', 'atomics']},
        'shaderImageFloat32AtomicAdd': {'python_name': ['shader', 'image', 'float32', 'atomic', 'add']},
        'sparseImageFloat32Atomics': {'python_name': ['sparse', 'image', 'float32', 'atomics']},
        'sparseImageFloat32AtomicAdd': {'python_name': ['sparse', 'image', 'float32', 'atomic', 'add']},
    }
}
