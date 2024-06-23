import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('matrix', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkAccelerationStructureInstanceKHR',
        'VkAccelerationStructureMatrixMotionInstanceNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'matrix': {'python_name': ['matrix']},
    }
}
