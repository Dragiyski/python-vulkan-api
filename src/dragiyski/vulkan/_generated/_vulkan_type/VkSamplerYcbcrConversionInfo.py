import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('conversion', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkImageViewCreateInfo',
        'VkSamplerCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'conversion': {'python_name': ['conversion']},
    }
}
