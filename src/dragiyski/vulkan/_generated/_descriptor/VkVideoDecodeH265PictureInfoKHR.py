from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeH265PictureInfoKHR'
_member_list_ = ['sType', 'pNext', 'pStdPictureInfo', 'sliceSegmentCount', 'pSliceSegmentOffsets']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_PICTURE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pStdPictureInfo': {
        'type': CPointerType(CComplexType('StdVideoDecodeH265PictureInfo')),
        'type_name': 'StdVideoDecodeH265PictureInfo',
        'structure': 'StdVideoDecodeH265PictureInfo',
        'is_string': False,
    },
    'sliceSegmentCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSliceSegmentOffsets': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['sliceSegmentCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoDecodeInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoDecodeH265PictureInfo',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
