import ctypes

class StdVideoAV1CDEF(ctypes.Structure):
    _fields_ = [
        ('cdef_damping_minus_3', ctypes.c_uint8),
        ('cdef_bits', ctypes.c_uint8),
        ('cdef_y_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_y_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_pri_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('cdef_uv_sec_strength', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeAV1PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'cdef_damping_minus_3': 'cdef_damping_minus_3',
        'cdef_bits': 'cdef_bits',
        'cdef_y_pri_strength': 'cdef_y_pri_strength',
        'cdef_y_sec_strength': 'cdef_y_sec_strength',
        'cdef_uv_pri_strength': 'cdef_uv_pri_strength',
        'cdef_uv_sec_strength': 'cdef_uv_sec_strength',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoAV1CDEF._type_ = {
    'cdef_damping_minus_3': ctypes.c_uint8,
    'cdef_bits': ctypes.c_uint8,
    'cdef_y_pri_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
    'cdef_y_sec_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
    'cdef_uv_pri_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
    'cdef_uv_sec_strength': ctypes.ARRAY(ctypes.c_uint8, 8),
}
