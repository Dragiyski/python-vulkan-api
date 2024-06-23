import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264SliceHeader import CType as StdVideoEncodeH264SliceHeader

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceHeader', ctypes.POINTER(StdVideoEncodeH264SliceHeader)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264SliceHeader',
    },
    'included_in': {
        'VkVideoEncodeH264PictureInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_NALU_SLICE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'constantQp': {'python_name': ['constant', 'qp']},
        'pStdSliceHeader': {'python_name': ['p', 'std', 'slice', 'header'], 'type': 'StdVideoEncodeH264SliceHeader'},
    }
}
