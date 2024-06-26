import ctypes

class StdVideoEncodeH265ReferenceListsInfoFlags(ctypes.Structure):
    _fields_ = [
        ('ref_pic_list_modification_flag_l0', ctypes.c_uint32, 1),
        ('ref_pic_list_modification_flag_l1', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoEncodeH265ReferenceListsInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'ref_pic_list_modification_flag_l0': 'ref_pic_list_modification_flag_l0',
        'ref_pic_list_modification_flag_l1': 'ref_pic_list_modification_flag_l1',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_encode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH265ReferenceListsInfoFlags._type_ = {
    'ref_pic_list_modification_flag_l0': ctypes.c_uint32,
    'ref_pic_list_modification_flag_l1': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
