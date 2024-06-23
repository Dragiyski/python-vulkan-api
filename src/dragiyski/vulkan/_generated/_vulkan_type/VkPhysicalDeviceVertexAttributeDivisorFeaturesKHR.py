import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vertexAttributeInstanceRateDivisor', ctypes.c_uint32),
        ('vertexAttributeInstanceRateZeroDivisor', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VERTEX_ATTRIBUTE_DIVISOR_FEATURES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'vertexAttributeInstanceRateDivisor': {'python_name': ['vertex', 'attribute', 'instance', 'rate', 'divisor']},
        'vertexAttributeInstanceRateZeroDivisor': {'python_name': ['vertex', 'attribute', 'instance', 'rate', 'zero', 'divisor']},
    }
}
