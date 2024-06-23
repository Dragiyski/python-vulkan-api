import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('postMergeSubpassCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRenderPassCreationFeedbackCreateInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'postMergeSubpassCount': {'python_name': ['post', 'merge', 'subpass', 'count']},
    }
}
