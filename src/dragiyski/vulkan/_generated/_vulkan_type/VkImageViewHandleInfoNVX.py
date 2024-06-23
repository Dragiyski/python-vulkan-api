import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('descriptorType', ctypes.c_int),
        ('sampler', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetImageViewHandleNVX',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_HANDLE_INFO_NVX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageView': {'python_name': ['image', 'view']},
        'descriptorType': {'python_name': ['descriptor', 'type'], 'type': 'VkDescriptorType'},
        'sampler': {'python_name': ['sampler']},
    }
}
