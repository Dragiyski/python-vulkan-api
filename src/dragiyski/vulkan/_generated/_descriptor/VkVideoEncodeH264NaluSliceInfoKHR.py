from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264NaluSliceInfoKHR'
_member_list_ = ['sType', 'pNext', 'constantQp', 'pStdSliceHeader']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_NALU_SLICE_INFO_KHR',
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
    'pStdSliceHeader': {
        'type': CPointerType(CComplexType('StdVideoEncodeH264SliceHeader')),
        'type_name': 'StdVideoEncodeH264SliceHeader',
        'structure': 'StdVideoEncodeH264SliceHeader',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH264SliceHeader',
}
_included_in_ = {
    'VkVideoEncodeH264PictureInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
