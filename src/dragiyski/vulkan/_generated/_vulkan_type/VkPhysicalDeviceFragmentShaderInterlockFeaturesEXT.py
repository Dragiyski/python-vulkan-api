import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShaderSampleInterlock', ctypes.c_uint32),
        ('fragmentShaderPixelInterlock', ctypes.c_uint32),
        ('fragmentShaderShadingRateInterlock', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADER_INTERLOCK_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fragmentShaderSampleInterlock': {'python_name': ['fragment', 'shader', 'sample', 'interlock']},
        'fragmentShaderPixelInterlock': {'python_name': ['fragment', 'shader', 'pixel', 'interlock']},
        'fragmentShaderShadingRateInterlock': {'python_name': ['fragment', 'shader', 'shading', 'rate', 'interlock']},
    }
}
