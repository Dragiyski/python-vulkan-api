from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeH264PictureInfoKHR'
_member_list_ = ['sType', 'pNext', 'pStdPictureInfo', 'sliceCount', 'pSliceOffsets']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PICTURE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pStdPictureInfo': {
        'type': CPointerType(CComplexType('StdVideoDecodeH264PictureInfo')),
        'type_name': 'StdVideoDecodeH264PictureInfo',
        'structure': 'StdVideoDecodeH264PictureInfo',
        'is_string': False,
    },
    'sliceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSliceOffsets': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['sliceCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoDecodeInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoDecodeH264PictureInfo',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
