import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('linearTilingFeatures', ctypes.c_uint32),
        ('optimalTilingFeatures', ctypes.c_uint32),
        ('bufferFeatures', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkFormatProperties2',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceFormatProperties',
    },
    'member_map': {
        'linearTilingFeatures': {'python_name': ['linear', 'tiling', 'features'], 'type': 'VkFormatFeatureFlags'},
        'optimalTilingFeatures': {'python_name': ['optimal', 'tiling', 'features'], 'type': 'VkFormatFeatureFlags'},
        'bufferFeatures': {'python_name': ['buffer', 'features'], 'type': 'VkFormatFeatureFlags'},
    }
}
