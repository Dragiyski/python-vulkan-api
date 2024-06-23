import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('coverageReductionMode', ctypes.c_int),
        ('rasterizationSamples', ctypes.c_uint32),
        ('depthStencilSamples', ctypes.c_uint32),
        ('colorSamples', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceSupportedFramebufferMixedSamplesCombinationsNV',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_MIXED_SAMPLES_COMBINATION_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'coverageReductionMode': {'python_name': ['coverage', 'reduction', 'mode'], 'type': 'VkCoverageReductionModeNV'},
        'rasterizationSamples': {'python_name': ['rasterization', 'samples'], 'type': 'VkSampleCountFlagBits'},
        'depthStencilSamples': {'python_name': ['depth', 'stencil', 'samples'], 'type': 'VkSampleCountFlags'},
        'colorSamples': {'python_name': ['color', 'samples'], 'type': 'VkSampleCountFlags'},
    }
}
