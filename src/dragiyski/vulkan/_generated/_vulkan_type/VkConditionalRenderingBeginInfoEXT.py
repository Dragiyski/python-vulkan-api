import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdBeginConditionalRenderingEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_CONDITIONAL_RENDERING_BEGIN_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'buffer': {'python_name': ['buffer']},
        'offset': {'python_name': ['offset']},
        'flags': {'python_name': ['flags'], 'type': 'VkConditionalRenderingFlagsEXT'},
    }
}
