import ctypes

class VkSRTDataNV(ctypes.Structure):
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

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkAccelerationStructureSRTMotionInstanceNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sx': 'sx',
        'a': 'a',
        'b': 'b',
        'pvx': 'pvx',
        'sy': 'sy',
        'c': 'c',
        'pvy': 'pvy',
        'sz': 'sz',
        'pvz': 'pvz',
        'qx': 'qx',
        'qy': 'qy',
        'qz': 'qz',
        'qw': 'qw',
        'tx': 'tx',
        'ty': 'ty',
        'tz': 'tz',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing_motion_blur',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkSRTDataNV._type_ = {
    'sx': ctypes.c_float,
    'a': ctypes.c_float,
    'b': ctypes.c_float,
    'pvx': ctypes.c_float,
    'sy': ctypes.c_float,
    'c': ctypes.c_float,
    'pvy': ctypes.c_float,
    'sz': ctypes.c_float,
    'pvz': ctypes.c_float,
    'qx': ctypes.c_float,
    'qy': ctypes.c_float,
    'qz': ctypes.c_float,
    'qw': ctypes.c_float,
    'tx': ctypes.c_float,
    'ty': ctypes.c_float,
    'tz': ctypes.c_float,
}
