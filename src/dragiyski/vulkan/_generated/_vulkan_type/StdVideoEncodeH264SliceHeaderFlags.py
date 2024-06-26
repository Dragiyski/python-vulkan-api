import ctypes

class StdVideoEncodeH264SliceHeaderFlags(ctypes.Structure):
    _fields_ = [
        ('direct_spatial_mv_pred_flag', ctypes.c_uint32, 1),
        ('num_ref_idx_active_override_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoEncodeH264SliceHeader',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'direct_spatial_mv_pred_flag': 'direct_spatial_mv_pred_flag',
        'num_ref_idx_active_override_flag': 'num_ref_idx_active_override_flag',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_encode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH264SliceHeaderFlags._type_ = {
    'direct_spatial_mv_pred_flag': ctypes.c_uint32,
    'num_ref_idx_active_override_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
