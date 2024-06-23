import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maximumRequestedAlignment', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_ALIGNMENT_CONTROL_CREATE_INFO_MESA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maximumRequestedAlignment': {'python_name': ['maximum', 'requested', 'alignment']},
    }
}
