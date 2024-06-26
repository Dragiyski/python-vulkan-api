import ctypes

class StdVideoEncodeH264RefPicMarkingEntry(ctypes.Structure):
    _fields_ = [
        ('memory_management_control_operation', ctypes.c_int),
        ('difference_of_pic_nums_minus1', ctypes.c_uint16),
        ('long_term_pic_num', ctypes.c_uint16),
        ('long_term_frame_idx', ctypes.c_uint16),
        ('max_long_term_frame_idx_plus1', ctypes.c_uint16),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoEncodeH264ReferenceListsInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'memory_management_control_operation': 'memory_management_control_operation',
        'difference_of_pic_nums_minus1': 'difference_of_pic_nums_minus1',
        'long_term_pic_num': 'long_term_pic_num',
        'long_term_frame_idx': 'long_term_frame_idx',
        'max_long_term_frame_idx_plus1': 'max_long_term_frame_idx_plus1',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_encode',
    }
    _vk_enum_ = {
        'memory_management_control_operation': 'StdVideoH264MemMgmtControlOp',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH264RefPicMarkingEntry._type_ = {
    'memory_management_control_operation': ctypes.c_int,
    'difference_of_pic_nums_minus1': ctypes.c_uint16,
    'long_term_pic_num': ctypes.c_uint16,
    'long_term_frame_idx': ctypes.c_uint16,
    'max_long_term_frame_idx_plus1': ctypes.c_uint16,
}
