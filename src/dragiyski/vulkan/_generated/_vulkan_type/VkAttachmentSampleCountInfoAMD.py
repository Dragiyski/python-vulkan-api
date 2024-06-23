import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentSamples', ctypes.POINTER(ctypes.c_uint32)),
        ('depthStencilAttachmentSamples', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkCommandBufferInheritanceInfo',
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ATTACHMENT_SAMPLE_COUNT_INFO_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'colorAttachmentCount': {'python_name': ['color', 'attachment', 'count']},
        'pColorAttachmentSamples': {'python_name': ['p', 'color', 'attachment', 'samples'], 'len': [['colorAttachmentCount']], 'type': 'VkSampleCountFlagBits'},
        'depthStencilAttachmentSamples': {'python_name': ['depth', 'stencil', 'attachment', 'samples'], 'type': 'VkSampleCountFlagBits'},
    }
}
