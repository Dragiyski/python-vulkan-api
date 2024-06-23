import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilInitialLayout', ctypes.c_int),
        ('stencilFinalLayout', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkAttachmentDescription2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_DESCRIPTION_STENCIL_LAYOUT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stencilInitialLayout': {'python_name': ['stencil', 'initial', 'layout'], 'type': 'VkImageLayout'},
        'stencilFinalLayout': {'python_name': ['stencil', 'final', 'layout'], 'type': 'VkImageLayout'},
    }
}
