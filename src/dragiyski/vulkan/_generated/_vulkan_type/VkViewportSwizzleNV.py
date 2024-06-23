import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),
        ('w', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineViewportSwizzleStateCreateInfoNV',
    },
    'input_of': {
        'vkCmdSetViewportSwizzleNV',
    },
    'output_of': set(),
    'member_map': {
        'x': {'python_name': ['x'], 'type': 'VkViewportCoordinateSwizzleNV'},
        'y': {'python_name': ['y'], 'type': 'VkViewportCoordinateSwizzleNV'},
        'z': {'python_name': ['z'], 'type': 'VkViewportCoordinateSwizzleNV'},
        'w': {'python_name': ['w'], 'type': 'VkViewportCoordinateSwizzleNV'},
    }
}
