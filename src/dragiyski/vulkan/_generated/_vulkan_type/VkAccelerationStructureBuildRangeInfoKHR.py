import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('primitiveCount', ctypes.c_uint32),
        ('primitiveOffset', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('transformOffset', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkBuildAccelerationStructuresKHR',
        'vkCmdBuildAccelerationStructuresKHR',
    },
    'output_of': set(),
    'member_map': {
        'primitiveCount': {'python_name': ['primitive', 'count']},
        'primitiveOffset': {'python_name': ['primitive', 'offset']},
        'firstVertex': {'python_name': ['first', 'vertex']},
        'transformOffset': {'python_name': ['transform', 'offset']},
    }
}
