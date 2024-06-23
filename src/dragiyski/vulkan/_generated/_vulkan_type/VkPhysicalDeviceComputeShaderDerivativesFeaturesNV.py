import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('computeDerivativeGroupQuads', ctypes.c_uint32),
        ('computeDerivativeGroupLinear', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_COMPUTE_SHADER_DERIVATIVES_FEATURES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'computeDerivativeGroupQuads': {'python_name': ['compute', 'derivative', 'group', 'quads']},
        'computeDerivativeGroupLinear': {'python_name': ['compute', 'derivative', 'group', 'linear']},
    }
}
