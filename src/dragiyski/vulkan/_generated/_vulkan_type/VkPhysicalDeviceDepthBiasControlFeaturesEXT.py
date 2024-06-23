import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasControl', ctypes.c_uint32),
        ('leastRepresentableValueForceUnormRepresentation', ctypes.c_uint32),
        ('floatRepresentation', ctypes.c_uint32),
        ('depthBiasExact', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEPTH_BIAS_CONTROL_FEATURES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'depthBiasControl': {'python_name': ['depth', 'bias', 'control']},
        'leastRepresentableValueForceUnormRepresentation': {'python_name': ['least', 'representable', 'value', 'force', 'unorm', 'representation']},
        'floatRepresentation': {'python_name': ['float', 'representation']},
        'depthBiasExact': {'python_name': ['depth', 'bias', 'exact']},
    }
}
