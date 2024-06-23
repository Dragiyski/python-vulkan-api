import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('xcoeff', ctypes.c_float),
        ('ycoeff', ctypes.c_float),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineViewportWScalingStateCreateInfoNV',
    },
    'input_of': {
        'vkCmdSetViewportWScalingNV',
    },
    'output_of': set(),
    'member_map': {
        'xcoeff': {'python_name': ['xcoeff']},
        'ycoeff': {'python_name': ['ycoeff']},
    }
}
