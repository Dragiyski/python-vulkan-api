import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('enableYDegamma', ctypes.c_uint32),
        ('enableCbCrDegamma', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkSamplerYcbcrConversionCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_YCBCR_DEGAMMA_CREATE_INFO_QCOM', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'enableYDegamma': {'python_name': ['enable', 'ydegamma']},
        'enableCbCrDegamma': {'python_name': ['enable', 'cb', 'cr', 'degamma']},
    }
}
