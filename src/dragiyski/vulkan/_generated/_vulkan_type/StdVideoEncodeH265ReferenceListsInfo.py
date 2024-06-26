import ctypes

class StdVideoEncodeH265ReferenceListsInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH265ReferenceListsInfoFlags',
    }
    _included_in_ = {
        'StdVideoEncodeH265PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'num_ref_idx_l0_active_minus1': 'num_ref_idx_l0_active_minus1',
        'num_ref_idx_l1_active_minus1': 'num_ref_idx_l1_active_minus1',
        'RefPicList0': 'ref_pic_list0',
        'RefPicList1': 'ref_pic_list1',
        'list_entry_l0': 'list_entry_l0',
        'list_entry_l1': 'list_entry_l1',
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


from .StdVideoEncodeH265ReferenceListsInfoFlags import StdVideoEncodeH265ReferenceListsInfoFlags

StdVideoEncodeH265ReferenceListsInfo._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceListsInfoFlags),
    ('num_ref_idx_l0_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_active_minus1', ctypes.c_uint8),
    ('RefPicList0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('RefPicList1', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l0', ctypes.ARRAY(ctypes.c_uint8, 15)),
    ('list_entry_l1', ctypes.ARRAY(ctypes.c_uint8, 15)),
]

StdVideoEncodeH265ReferenceListsInfo._type_ = {
    'flags': StdVideoEncodeH265ReferenceListsInfoFlags,
    'num_ref_idx_l0_active_minus1': ctypes.c_uint8,
    'num_ref_idx_l1_active_minus1': ctypes.c_uint8,
    'RefPicList0': ctypes.ARRAY(ctypes.c_uint8, 15),
    'RefPicList1': ctypes.ARRAY(ctypes.c_uint8, 15),
    'list_entry_l0': ctypes.ARRAY(ctypes.c_uint8, 15),
    'list_entry_l1': ctypes.ARRAY(ctypes.c_uint8, 15),
}
