import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('contents', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdBeginRenderPass2',
        'vkCmdNextSubpass2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_BEGIN_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'contents': {'python_name': ['contents'], 'type': 'VkSubpassContents'},
    }
}
