import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreMask', ctypes.c_uint64),
        ('shaderCoreCount', ctypes.c_uint32),
        ('shaderWarpsPerCore', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADER_CORE_BUILTINS_PROPERTIES_ARM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shaderCoreMask': {'python_name': ['shader', 'core', 'mask']},
        'shaderCoreCount': {'python_name': ['shader', 'core', 'count']},
        'shaderWarpsPerCore': {'python_name': ['shader', 'warps', 'per', 'core']},
    }
}
