import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265SliceSegmentHeader import CType as StdVideoEncodeH265SliceSegmentHeader

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceSegmentHeader', ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH265SliceSegmentHeader',
    },
    'included_in': {
        'VkVideoEncodeH265PictureInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_NALU_SLICE_SEGMENT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'constantQp': {'python_name': ['constant', 'qp']},
        'pStdSliceSegmentHeader': {'python_name': ['p', 'std', 'slice', 'segment', 'header'], 'type': 'StdVideoEncodeH265SliceSegmentHeader'},
    }
}
