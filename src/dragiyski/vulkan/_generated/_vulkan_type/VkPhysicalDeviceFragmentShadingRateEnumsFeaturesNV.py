import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShadingRateEnums', ctypes.c_uint32),
        ('supersampleFragmentShadingRates', ctypes.c_uint32),
        ('noInvocationFragmentShadingRates', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_FEATURES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fragmentShadingRateEnums': {'python_name': ['fragment', 'shading', 'rate', 'enums']},
        'supersampleFragmentShadingRates': {'python_name': ['supersample', 'fragment', 'shading', 'rates']},
        'noInvocationFragmentShadingRates': {'python_name': ['no', 'invocation', 'fragment', 'shading', 'rates']},
    }
}
