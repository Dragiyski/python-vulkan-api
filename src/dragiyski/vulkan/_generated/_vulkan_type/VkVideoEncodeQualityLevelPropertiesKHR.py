import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('preferredRateControlMode', ctypes.c_uint32),
        ('preferredRateControlLayerCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoEncodeH264QualityLevelPropertiesKHR',
        'VkVideoEncodeH265QualityLevelPropertiesKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceVideoEncodeQualityLevelPropertiesKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_QUALITY_LEVEL_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'preferredRateControlMode': {'python_name': ['preferred', 'rate', 'control', 'mode'], 'type': 'VkVideoEncodeRateControlModeFlagBitsKHR'},
        'preferredRateControlLayerCount': {'python_name': ['preferred', 'rate', 'control', 'layer', 'count']},
    }
}
