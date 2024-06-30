from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265PictureInfoKHR'
_member_list_ = ['sType', 'pNext', 'naluSliceSegmentEntryCount', 'pNaluSliceSegmentEntries', 'pStdPictureInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_PICTURE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'naluSliceSegmentEntryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pNaluSliceSegmentEntries': {
        'type': CPointerType(CComplexType('VkVideoEncodeH265NaluSliceSegmentInfoKHR')),
        'type_name': 'VkVideoEncodeH265NaluSliceSegmentInfoKHR',
        'structure': 'VkVideoEncodeH265NaluSliceSegmentInfoKHR',
        'length': [['naluSliceSegmentEntryCount']],
        'is_string': False,
    },
    'pStdPictureInfo': {
        'type': CPointerType(CComplexType('StdVideoEncodeH265PictureInfo')),
        'type_name': 'StdVideoEncodeH265PictureInfo',
        'structure': 'StdVideoEncodeH265PictureInfo',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoEncodeInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265PictureInfo',
    'VkVideoEncodeH265NaluSliceSegmentInfoKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
