import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('viewFormatCount', ctypes.c_uint32),
        ('pViewFormats', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
        'VkPhysicalDeviceImageFormatInfo2',
        'VkSwapchainCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_FORMAT_LIST_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'viewFormatCount': {'python_name': ['view', 'format', 'count']},
        'pViewFormats': {'python_name': ['p', 'view', 'formats'], 'len': [['viewFormatCount']], 'type': 'VkFormat'},
    }
}
