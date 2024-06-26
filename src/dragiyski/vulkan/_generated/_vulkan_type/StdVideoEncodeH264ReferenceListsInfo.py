import ctypes

class StdVideoEncodeH264ReferenceListsInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH264RefListModEntry',
        'StdVideoEncodeH264RefPicMarkingEntry',
        'StdVideoEncodeH264ReferenceListsInfoFlags',
    }
    _included_in_ = {
        'StdVideoEncodeH264PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'num_ref_idx_l0_active_minus1': 'num_ref_idx_l0_active_minus1',
        'num_ref_idx_l1_active_minus1': 'num_ref_idx_l1_active_minus1',
        'RefPicList0': 'ref_pic_list0',
        'RefPicList1': 'ref_pic_list1',
        'refList0ModOpCount': 'ref_list0_mod_op_count',
        'refList1ModOpCount': 'ref_list1_mod_op_count',
        'refPicMarkingOpCount': 'ref_pic_marking_op_count',
        'reserved1': 'reserved1',
        'pRefList0ModOperations': 'ref_list0_mod_operations',
        'pRefList1ModOperations': 'ref_list1_mod_operations',
        'pRefPicMarkingOperations': 'ref_pic_marking_operations',
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


from .StdVideoEncodeH264RefListModEntry import StdVideoEncodeH264RefListModEntry
from .StdVideoEncodeH264RefPicMarkingEntry import StdVideoEncodeH264RefPicMarkingEntry
from .StdVideoEncodeH264ReferenceListsInfoFlags import StdVideoEncodeH264ReferenceListsInfoFlags

StdVideoEncodeH264ReferenceListsInfo._fields_ = [
    ('flags', StdVideoEncodeH264ReferenceListsInfoFlags),
    ('num_ref_idx_l0_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_active_minus1', ctypes.c_uint8),
    ('RefPicList0', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ('RefPicList1', ctypes.ARRAY(ctypes.c_uint8, 32)),
    ('refList0ModOpCount', ctypes.c_uint8),
    ('refList1ModOpCount', ctypes.c_uint8),
    ('refPicMarkingOpCount', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('pRefList0ModOperations', ctypes.POINTER(StdVideoEncodeH264RefListModEntry)),
    ('pRefList1ModOperations', ctypes.POINTER(StdVideoEncodeH264RefListModEntry)),
    ('pRefPicMarkingOperations', ctypes.POINTER(StdVideoEncodeH264RefPicMarkingEntry)),
]

StdVideoEncodeH264ReferenceListsInfo._type_ = {
    'flags': StdVideoEncodeH264ReferenceListsInfoFlags,
    'num_ref_idx_l0_active_minus1': ctypes.c_uint8,
    'num_ref_idx_l1_active_minus1': ctypes.c_uint8,
    'RefPicList0': ctypes.ARRAY(ctypes.c_uint8, 32),
    'RefPicList1': ctypes.ARRAY(ctypes.c_uint8, 32),
    'refList0ModOpCount': ctypes.c_uint8,
    'refList1ModOpCount': ctypes.c_uint8,
    'refPicMarkingOpCount': ctypes.c_uint8,
    'reserved1': ctypes.ARRAY(ctypes.c_uint8, 7),
    'pRefList0ModOperations': ctypes.POINTER(StdVideoEncodeH264RefListModEntry),
    'pRefList1ModOperations': ctypes.POINTER(StdVideoEncodeH264RefListModEntry),
    'pRefPicMarkingOperations': ctypes.POINTER(StdVideoEncodeH264RefPicMarkingEntry),
}
