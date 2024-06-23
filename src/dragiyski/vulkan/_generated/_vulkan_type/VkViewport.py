import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
        ('width', ctypes.c_float),
        ('height', ctypes.c_float),
        ('minDepth', ctypes.c_float),
        ('maxDepth', ctypes.c_float),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkCommandBufferInheritanceViewportScissorInfoNV',
        'VkPipelineViewportStateCreateInfo',
    },
    'input_of': {
        'vkCmdSetViewport',
        'vkCmdSetViewportWithCount',
    },
    'output_of': set(),
    'member_map': {
        'x': {'python_name': ['x']},
        'y': {'python_name': ['y']},
        'width': {'python_name': ['width']},
        'height': {'python_name': ['height']},
        'minDepth': {'python_name': ['min', 'depth']},
        'maxDepth': {'python_name': ['max', 'depth']},
    }
}
