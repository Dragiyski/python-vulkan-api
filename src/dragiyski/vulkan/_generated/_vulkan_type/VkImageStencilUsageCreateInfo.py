import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilUsage', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
        'VkPhysicalDeviceImageFormatInfo2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_STENCIL_USAGE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stencilUsage': {'python_name': ['stencil', 'usage'], 'type': 'VkImageUsageFlags'},
    }
}
