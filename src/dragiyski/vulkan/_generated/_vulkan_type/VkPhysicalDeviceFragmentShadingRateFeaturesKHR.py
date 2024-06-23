import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineFragmentShadingRate', ctypes.c_uint32),
        ('primitiveFragmentShadingRate', ctypes.c_uint32),
        ('attachmentFragmentShadingRate', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_FEATURES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pipelineFragmentShadingRate': {'python_name': ['pipeline', 'fragment', 'shading', 'rate']},
        'primitiveFragmentShadingRate': {'python_name': ['primitive', 'fragment', 'shading', 'rate']},
        'attachmentFragmentShadingRate': {'python_name': ['attachment', 'fragment', 'shading', 'rate']},
    }
}
