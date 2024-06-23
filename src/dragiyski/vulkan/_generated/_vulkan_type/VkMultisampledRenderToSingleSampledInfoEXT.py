import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('multisampledRenderToSingleSampledEnable', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkRenderingInfo',
        'VkSubpassDescription2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MULTISAMPLED_RENDER_TO_SINGLE_SAMPLED_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'multisampledRenderToSingleSampledEnable': {'python_name': ['multisampled', 'render', 'to', 'single', 'sampled', 'enable']},
        'rasterizationSamples': {'python_name': ['rasterization', 'samples'], 'type': 'VkSampleCountFlagBits'},
    }
}
