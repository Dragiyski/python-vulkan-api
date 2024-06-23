import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('linearTilingFeatures', ctypes.c_uint64),
        ('optimalTilingFeatures', ctypes.c_uint64),
        ('bufferFeatures', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkFormatProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FORMAT_PROPERTIES_3', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'linearTilingFeatures': {'python_name': ['linear', 'tiling', 'features'], 'type': 'VkFormatFeatureFlags2'},
        'optimalTilingFeatures': {'python_name': ['optimal', 'tiling', 'features'], 'type': 'VkFormatFeatureFlags2'},
        'bufferFeatures': {'python_name': ['buffer', 'features'], 'type': 'VkFormatFeatureFlags2'},
    }
}
