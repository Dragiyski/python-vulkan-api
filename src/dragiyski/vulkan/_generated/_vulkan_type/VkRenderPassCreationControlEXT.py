import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('disallowMerging', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkRenderPassCreateInfo2',
        'VkSubpassDescription2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_CREATION_CONTROL_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'disallowMerging': {'python_name': ['disallow', 'merging']},
    }
}
