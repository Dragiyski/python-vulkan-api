import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('renderPass', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pAttachments', ctypes.POINTER(ctypes.c_void_p)),
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('layers', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkFramebufferAttachmentsCreateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateFramebuffer',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FRAMEBUFFER_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkFramebufferCreateFlags'},
        'renderPass': {'python_name': ['render', 'pass']},
        'attachmentCount': {'python_name': ['attachment', 'count']},
        'pAttachments': {'python_name': ['p', 'attachments'], 'len': [['attachmentCount']]},
        'width': {'python_name': ['width']},
        'height': {'python_name': ['height']},
        'layers': {'python_name': ['layers']},
    }
}
