import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('subpass', ctypes.c_uint32),
        ('inputAttachmentIndex', ctypes.c_uint32),
        ('aspectMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRenderPassInputAttachmentAspectCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'subpass': {'python_name': ['subpass']},
        'inputAttachmentIndex': {'python_name': ['input', 'attachment', 'index']},
        'aspectMask': {'python_name': ['aspect', 'mask'], 'type': 'VkImageAspectFlags'},
    }
}
