import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentInputIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pDepthInputAttachmentIndex', ctypes.POINTER(ctypes.c_uint32)),
        ('pStencilInputAttachmentIndex', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkCommandBufferInheritanceInfo',
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetRenderingInputAttachmentIndicesKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDERING_INPUT_ATTACHMENT_INDEX_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'colorAttachmentCount': {'python_name': ['color', 'attachment', 'count']},
        'pColorAttachmentInputIndices': {'python_name': ['p', 'color', 'attachment', 'input', 'indices'], 'len': [['colorAttachmentCount']]},
        'pDepthInputAttachmentIndex': {'python_name': ['p', 'depth', 'input', 'attachment', 'index']},
        'pStencilInputAttachmentIndex': {'python_name': ['p', 'stencil', 'input', 'attachment', 'index']},
    }
}
