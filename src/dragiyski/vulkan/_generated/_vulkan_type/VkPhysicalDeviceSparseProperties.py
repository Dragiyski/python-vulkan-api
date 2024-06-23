import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('residencyStandard2DBlockShape', ctypes.c_uint32),
        ('residencyStandard2DMultisampleBlockShape', ctypes.c_uint32),
        ('residencyStandard3DBlockShape', ctypes.c_uint32),
        ('residencyAlignedMipSize', ctypes.c_uint32),
        ('residencyNonResidentStrict', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPhysicalDeviceProperties',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'residencyStandard2DBlockShape': {'python_name': ['residency', 'standard2', 'dblock', 'shape']},
        'residencyStandard2DMultisampleBlockShape': {'python_name': ['residency', 'standard2', 'dmultisample', 'block', 'shape']},
        'residencyStandard3DBlockShape': {'python_name': ['residency', 'standard3', 'dblock', 'shape']},
        'residencyAlignedMipSize': {'python_name': ['residency', 'aligned', 'mip', 'size']},
        'residencyNonResidentStrict': {'python_name': ['residency', 'non', 'resident', 'strict']},
    }
}
