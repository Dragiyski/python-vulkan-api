import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sx', ctypes.c_float),
        ('a', ctypes.c_float),
        ('b', ctypes.c_float),
        ('pvx', ctypes.c_float),
        ('sy', ctypes.c_float),
        ('c', ctypes.c_float),
        ('pvy', ctypes.c_float),
        ('sz', ctypes.c_float),
        ('pvz', ctypes.c_float),
        ('qx', ctypes.c_float),
        ('qy', ctypes.c_float),
        ('qz', ctypes.c_float),
        ('qw', ctypes.c_float),
        ('tx', ctypes.c_float),
        ('ty', ctypes.c_float),
        ('tz', ctypes.c_float),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkAccelerationStructureSRTMotionInstanceNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sx': {'python_name': ['sx']},
        'a': {'python_name': ['a']},
        'b': {'python_name': ['b']},
        'pvx': {'python_name': ['pvx']},
        'sy': {'python_name': ['sy']},
        'c': {'python_name': ['c']},
        'pvy': {'python_name': ['pvy']},
        'sz': {'python_name': ['sz']},
        'pvz': {'python_name': ['pvz']},
        'qx': {'python_name': ['qx']},
        'qy': {'python_name': ['qy']},
        'qz': {'python_name': ['qz']},
        'qw': {'python_name': ['qw']},
        'tx': {'python_name': ['tx']},
        'ty': {'python_name': ['ty']},
        'tz': {'python_name': ['tz']},
    }
}
