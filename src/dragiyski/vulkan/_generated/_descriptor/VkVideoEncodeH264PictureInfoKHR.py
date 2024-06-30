from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264PictureInfoKHR'
_member_list_ = ['sType', 'pNext', 'naluSliceEntryCount', 'pNaluSliceEntries', 'pStdPictureInfo', 'generatePrefixNalu']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_PICTURE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'naluSliceEntryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pNaluSliceEntries': {
        'type': CPointerType(CComplexType('VkVideoEncodeH264NaluSliceInfoKHR')),
        'type_name': 'VkVideoEncodeH264NaluSliceInfoKHR',
        'structure': 'VkVideoEncodeH264NaluSliceInfoKHR',
        'length': [['naluSliceEntryCount']],
        'is_string': False,
    },
    'pStdPictureInfo': {
        'type': CPointerType(CComplexType('StdVideoEncodeH264PictureInfo')),
        'type_name': 'StdVideoEncodeH264PictureInfo',
        'structure': 'StdVideoEncodeH264PictureInfo',
        'is_string': False,
    },
    'generatePrefixNalu': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoEncodeInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH264PictureInfo',
    'VkVideoEncodeH264NaluSliceInfoKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
