import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('usage', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
        'VkPhysicalDeviceImageFormatInfo2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceOpticalFlowImageFormatsNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_IMAGE_FORMAT_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'usage': {'python_name': ['usage'], 'type': 'VkOpticalFlowUsageFlagsNV'},
    }
}
