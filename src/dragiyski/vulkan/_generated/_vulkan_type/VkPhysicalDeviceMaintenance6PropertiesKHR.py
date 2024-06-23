import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('blockTexelViewCompatibleMultipleLayers', ctypes.c_uint32),
        ('maxCombinedImageSamplerDescriptorCount', ctypes.c_uint32),
        ('fragmentShadingRateClampCombinerInputs', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MAINTENANCE_6_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'blockTexelViewCompatibleMultipleLayers': {'python_name': ['block', 'texel', 'view', 'compatible', 'multiple', 'layers']},
        'maxCombinedImageSamplerDescriptorCount': {'python_name': ['max', 'combined', 'image', 'sampler', 'descriptor', 'count']},
        'fragmentShadingRateClampCombinerInputs': {'python_name': ['fragment', 'shading', 'rate', 'clamp', 'combiner', 'inputs']},
    }
}
