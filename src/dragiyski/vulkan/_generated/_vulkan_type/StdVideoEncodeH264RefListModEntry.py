import ctypes

class StdVideoEncodeH264RefListModEntry(ctypes.Structure):
    _fields_ = [
        ('modification_of_pic_nums_idc', ctypes.c_int),
        ('abs_diff_pic_num_minus1', ctypes.c_uint16),
        ('long_term_pic_num', ctypes.c_uint16),
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
        'modification_of_pic_nums_idc': 'modification_of_pic_nums_idc',
        'abs_diff_pic_num_minus1': 'abs_diff_pic_num_minus1',
        'long_term_pic_num': 'long_term_pic_num',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_encode',
    }
    _vk_enum_ = {
        'modification_of_pic_nums_idc': 'StdVideoH264ModificationOfPicNumsIdc',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH264RefListModEntry._type_ = {
    'modification_of_pic_nums_idc': ctypes.c_int,
    'abs_diff_pic_num_minus1': ctypes.c_uint16,
    'long_term_pic_num': ctypes.c_uint16,
}
