import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('viewMask', ctypes.c_uint32),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentFormats', ctypes.POINTER(ctypes.c_int)),
        ('depthAttachmentFormat', ctypes.c_int),
        ('stencilAttachmentFormat', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_RENDERING_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'viewMask': {'python_name': ['view', 'mask']},
        'colorAttachmentCount': {'python_name': ['color', 'attachment', 'count']},
        'pColorAttachmentFormats': {'python_name': ['p', 'color', 'attachment', 'formats'], 'len': [['colorAttachmentCount']], 'type': 'VkFormat'},
        'depthAttachmentFormat': {'python_name': ['depth', 'attachment', 'format'], 'type': 'VkFormat'},
        'stencilAttachmentFormat': {'python_name': ['stencil', 'attachment', 'format'], 'type': 'VkFormat'},
    }
}
