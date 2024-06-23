import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minFragmentShadingRateAttachmentTexelSize', VkExtent2D),
    ('maxFragmentShadingRateAttachmentTexelSize', VkExtent2D),
    ('maxFragmentShadingRateAttachmentTexelSizeAspectRatio', ctypes.c_uint32),
    ('primitiveFragmentShadingRateWithMultipleViewports', ctypes.c_uint32),
    ('layeredShadingRateAttachments', ctypes.c_uint32),
    ('fragmentShadingRateNonTrivialCombinerOps', ctypes.c_uint32),
    ('maxFragmentSize', VkExtent2D),
    ('maxFragmentSizeAspectRatio', ctypes.c_uint32),
    ('maxFragmentShadingRateCoverageSamples', ctypes.c_uint32),
    ('maxFragmentShadingRateRasterizationSamples', ctypes.c_uint32),
    ('fragmentShadingRateWithShaderDepthStencilWrites', ctypes.c_uint32),
    ('fragmentShadingRateWithSampleMask', ctypes.c_uint32),
    ('fragmentShadingRateWithShaderSampleMask', ctypes.c_uint32),
    ('fragmentShadingRateWithConservativeRasterization', ctypes.c_uint32),
    ('fragmentShadingRateWithFragmentShaderInterlock', ctypes.c_uint32),
    ('fragmentShadingRateWithCustomSampleLocations', ctypes.c_uint32),
    ('fragmentShadingRateStrictMultiplyCombiner', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'minFragmentShadingRateAttachmentTexelSize': {'python_name': ['min', 'fragment', 'shading', 'rate', 'attachment', 'texel', 'size'], 'type': 'VkExtent2D'},
        'maxFragmentShadingRateAttachmentTexelSize': {'python_name': ['max', 'fragment', 'shading', 'rate', 'attachment', 'texel', 'size'], 'type': 'VkExtent2D'},
        'maxFragmentShadingRateAttachmentTexelSizeAspectRatio': {'python_name': ['max', 'fragment', 'shading', 'rate', 'attachment', 'texel', 'size', 'aspect', 'ratio']},
        'primitiveFragmentShadingRateWithMultipleViewports': {'python_name': ['primitive', 'fragment', 'shading', 'rate', 'with', 'multiple', 'viewports']},
        'layeredShadingRateAttachments': {'python_name': ['layered', 'shading', 'rate', 'attachments']},
        'fragmentShadingRateNonTrivialCombinerOps': {'python_name': ['fragment', 'shading', 'rate', 'non', 'trivial', 'combiner', 'ops']},
        'maxFragmentSize': {'python_name': ['max', 'fragment', 'size'], 'type': 'VkExtent2D'},
        'maxFragmentSizeAspectRatio': {'python_name': ['max', 'fragment', 'size', 'aspect', 'ratio']},
        'maxFragmentShadingRateCoverageSamples': {'python_name': ['max', 'fragment', 'shading', 'rate', 'coverage', 'samples']},
        'maxFragmentShadingRateRasterizationSamples': {'python_name': ['max', 'fragment', 'shading', 'rate', 'rasterization', 'samples'], 'type': 'VkSampleCountFlagBits'},
        'fragmentShadingRateWithShaderDepthStencilWrites': {'python_name': ['fragment', 'shading', 'rate', 'with', 'shader', 'depth', 'stencil', 'writes']},
        'fragmentShadingRateWithSampleMask': {'python_name': ['fragment', 'shading', 'rate', 'with', 'sample', 'mask']},
        'fragmentShadingRateWithShaderSampleMask': {'python_name': ['fragment', 'shading', 'rate', 'with', 'shader', 'sample', 'mask']},
        'fragmentShadingRateWithConservativeRasterization': {'python_name': ['fragment', 'shading', 'rate', 'with', 'conservative', 'rasterization']},
        'fragmentShadingRateWithFragmentShaderInterlock': {'python_name': ['fragment', 'shading', 'rate', 'with', 'fragment', 'shader', 'interlock']},
        'fragmentShadingRateWithCustomSampleLocations': {'python_name': ['fragment', 'shading', 'rate', 'with', 'custom', 'sample', 'locations']},
        'fragmentShadingRateStrictMultiplyCombiner': {'python_name': ['fragment', 'shading', 'rate', 'strict', 'multiply', 'combiner']},
    }
}
