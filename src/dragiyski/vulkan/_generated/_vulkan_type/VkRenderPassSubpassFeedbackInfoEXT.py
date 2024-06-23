import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('subpassMergeStatus', ctypes.c_int),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('postMergeIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRenderPassSubpassFeedbackCreateInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'subpassMergeStatus': {'python_name': ['subpass', 'merge', 'status'], 'type': 'VkSubpassMergeStatusEXT'},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
        'postMergeIndex': {'python_name': ['post', 'merge', 'index']},
    }
}
