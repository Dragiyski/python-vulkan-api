from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeAV1PictureInfoKHR'
_member_list_ = ['sType', 'pNext', 'pStdPictureInfo', 'referenceNameSlotIndices', 'frameHeaderOffset', 'tileCount', 'pTileOffsets', 'pTileSizes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_PICTURE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pStdPictureInfo': {
        'type': CPointerType(CComplexType('StdVideoDecodeAV1PictureInfo')),
        'type_name': 'StdVideoDecodeAV1PictureInfo',
        'structure': 'StdVideoDecodeAV1PictureInfo',
        'is_string': False,
    },
    'referenceNameSlotIndices': {
        'type': CArrayType(CIntType('c_int32'), 7),
        'is_string': False,
    },
    'frameHeaderOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'tileCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pTileOffsets': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['tileCount']],
        'is_string': False,
    },
    'pTileSizes': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['tileCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoDecodeInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
