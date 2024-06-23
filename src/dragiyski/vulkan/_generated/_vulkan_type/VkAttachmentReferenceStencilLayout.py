import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilLayout', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkAttachmentReference2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_STENCIL_LAYOUT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stencilLayout': {'python_name': ['stencil', 'layout'], 'type': 'VkImageLayout'},
    }
}
