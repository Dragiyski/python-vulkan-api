import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('reductionMode', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkSamplerCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SAMPLER_REDUCTION_MODE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'reductionMode': {'python_name': ['reduction', 'mode'], 'type': 'VkSamplerReductionMode'},
    }
}
