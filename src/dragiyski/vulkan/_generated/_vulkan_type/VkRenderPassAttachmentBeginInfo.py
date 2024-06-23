import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pAttachments', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': {
        'VkRenderPassBeginInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_ATTACHMENT_BEGIN_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'attachmentCount': {'python_name': ['attachment', 'count']},
        'pAttachments': {'python_name': ['p', 'attachments'], 'len': [['attachmentCount']]},
    }
}
