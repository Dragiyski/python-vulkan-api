import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('numUsedVgprs', ctypes.c_uint32),
        ('numUsedSgprs', ctypes.c_uint32),
        ('ldsSizePerLocalWorkGroup', ctypes.c_uint32),
        ('ldsUsageSizeInBytes', ctypes.c_size_t),
        ('scratchMemUsageInBytes', ctypes.c_size_t),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkShaderStatisticsInfoAMD',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'numUsedVgprs': {'python_name': ['num', 'used', 'vgprs']},
        'numUsedSgprs': {'python_name': ['num', 'used', 'sgprs']},
        'ldsSizePerLocalWorkGroup': {'python_name': ['lds', 'size', 'per', 'local', 'work', 'group']},
        'ldsUsageSizeInBytes': {'python_name': ['lds', 'usage', 'size', 'in', 'bytes']},
        'scratchMemUsageInBytes': {'python_name': ['scratch', 'mem', 'usage', 'in', 'bytes']},
    }
}
