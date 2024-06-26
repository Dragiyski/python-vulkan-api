import ctypes

class StdVideoH264PpsFlags(ctypes.Structure):
    _fields_ = [
        ('transform_8x8_mode_flag', ctypes.c_uint32, 1),
        ('redundant_pic_cnt_present_flag', ctypes.c_uint32, 1),
        ('constrained_intra_pred_flag', ctypes.c_uint32, 1),
        ('deblocking_filter_control_present_flag', ctypes.c_uint32, 1),
        ('weighted_pred_flag', ctypes.c_uint32, 1),
        ('bottom_field_pic_order_in_frame_present_flag', ctypes.c_uint32, 1),
        ('entropy_coding_mode_flag', ctypes.c_uint32, 1),
        ('pic_scaling_matrix_present_flag', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH264PictureParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'transform_8x8_mode_flag': 'transform_8x8_mode_flag',
        'redundant_pic_cnt_present_flag': 'redundant_pic_cnt_present_flag',
        'constrained_intra_pred_flag': 'constrained_intra_pred_flag',
        'deblocking_filter_control_present_flag': 'deblocking_filter_control_present_flag',
        'weighted_pred_flag': 'weighted_pred_flag',
        'bottom_field_pic_order_in_frame_present_flag': 'bottom_field_pic_order_in_frame_present_flag',
        'entropy_coding_mode_flag': 'entropy_coding_mode_flag',
        'pic_scaling_matrix_present_flag': 'pic_scaling_matrix_present_flag',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoH264PpsFlags._type_ = {
    'transform_8x8_mode_flag': ctypes.c_uint32,
    'redundant_pic_cnt_present_flag': ctypes.c_uint32,
    'constrained_intra_pred_flag': ctypes.c_uint32,
    'deblocking_filter_control_present_flag': ctypes.c_uint32,
    'weighted_pred_flag': ctypes.c_uint32,
    'bottom_field_pic_order_in_frame_present_flag': ctypes.c_uint32,
    'entropy_coding_mode_flag': ctypes.c_uint32,
    'pic_scaling_matrix_present_flag': ctypes.c_uint32,
}
