from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265NaluSliceSegmentInfoKHR'
_member_list_ = ['sType', 'pNext', 'constantQp', 'pStdSliceSegmentHeader']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_NALU_SLICE_SEGMENT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'constantQp': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'pStdSliceSegmentHeader': {
        'type': CPointerType(CComplexType('StdVideoEncodeH265SliceSegmentHeader')),
        'type_name': 'StdVideoEncodeH265SliceSegmentHeader',
        'structure': 'StdVideoEncodeH265SliceSegmentHeader',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265SliceSegmentHeader',
}
_included_in_ = {
    'VkVideoEncodeH265PictureInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
