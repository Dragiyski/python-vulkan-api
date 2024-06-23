import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkSubpassFragmentDensityMapOffsetEndInfoQCOM',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdEndRenderPass2',
        'vkCmdNextSubpass2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_END_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
    }
}
