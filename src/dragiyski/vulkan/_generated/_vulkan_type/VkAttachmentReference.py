import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkRenderPassFragmentDensityMapCreateInfoEXT',
        'VkSubpassDescription',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'attachment': {'python_name': ['attachment']},
        'layout': {'python_name': ['layout'], 'type': 'VkImageLayout'},
    }
}
