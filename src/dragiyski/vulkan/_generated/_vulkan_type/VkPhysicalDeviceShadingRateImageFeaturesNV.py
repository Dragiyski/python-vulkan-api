import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shadingRateImage', ctypes.c_uint32),
        ('shadingRateCoarseSampleOrder', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SHADING_RATE_IMAGE_FEATURES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'shadingRateImage': {'python_name': ['shading', 'rate', 'image']},
        'shadingRateCoarseSampleOrder': {'python_name': ['shading', 'rate', 'coarse', 'sample', 'order']},
    }
}
