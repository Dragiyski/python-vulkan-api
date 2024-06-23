import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetImageViewAddressNVX',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_VIEW_ADDRESS_PROPERTIES_NVX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceAddress': {'python_name': ['device', 'address']},
        'size': {'python_name': ['size']},
    }
}
