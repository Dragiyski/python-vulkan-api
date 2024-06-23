import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
        ('aspectMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkAttachmentReferenceStencilLayout',
    },
    'includes': set(),
    'included_in': {
        'VkFragmentShadingRateAttachmentInfoKHR',
        'VkSubpassDescription2',
        'VkSubpassDescriptionDepthStencilResolve',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_REFERENCE_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'attachment': {'python_name': ['attachment']},
        'layout': {'python_name': ['layout'], 'type': 'VkImageLayout'},
        'aspectMask': {'python_name': ['aspect', 'mask'], 'type': 'VkImageAspectFlags'},
    }
}
