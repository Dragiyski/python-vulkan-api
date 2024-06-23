import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dedicatedAllocation', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEDICATED_ALLOCATION_IMAGE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'dedicatedAllocation': {'python_name': ['dedicated', 'allocation']},
    }
}
