import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageUsage', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoProfileListInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceVideoFormatPropertiesKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VIDEO_FORMAT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageUsage': {'python_name': ['image', 'usage'], 'type': 'VkImageUsageFlags'},
    }
}
