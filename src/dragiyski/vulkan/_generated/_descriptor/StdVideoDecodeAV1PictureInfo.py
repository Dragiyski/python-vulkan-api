from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeAV1PictureInfo'
_member_list_ = ['flags', 'frame_type', 'current_frame_id', 'OrderHint', 'primary_ref_frame', 'refresh_frame_flags', 'reserved1', 'interpolation_filter', 'TxMode', 'delta_q_res', 'delta_lf_res', 'SkipModeFrame', 'coded_denom', 'reserved2', 'OrderHints', 'expectedFrameId', 'pTileInfo', 'pQuantization', 'pSegmentation', 'pLoopFilter', 'pCDEF', 'pLoopRestoration', 'pGlobalMotion', 'pFilmGrain']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoDecodeAV1PictureInfoFlags'),
        'type_name': 'StdVideoDecodeAV1PictureInfoFlags',
        'structure': 'StdVideoDecodeAV1PictureInfoFlags',
        'is_string': False,
    },
    'frame_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1FrameType',
        'enum': 'StdVideoAV1FrameType',
        'is_string': False,
    },
    'current_frame_id': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'OrderHint': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'primary_ref_frame': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'refresh_frame_flags': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'interpolation_filter': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1InterpolationFilter',
        'enum': 'StdVideoAV1InterpolationFilter',
        'is_string': False,
    },
    'TxMode': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1TxMode',
        'enum': 'StdVideoAV1TxMode',
        'is_string': False,
    },
    'delta_q_res': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'delta_lf_res': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'SkipModeFrame': {
        'type': CArrayType(CIntType('c_uint8'), 2),
        'is_string': False,
    },
    'coded_denom': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved2': {
        'type': CArrayType(CIntType('c_uint8'), 3),
        'is_string': False,
    },
    'OrderHints': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'expectedFrameId': {
        'type': CArrayType(CIntType('c_uint32'), 8),
        'is_string': False,
    },
    'pTileInfo': {
        'type': CPointerType(CComplexType('StdVideoAV1TileInfo')),
        'type_name': 'StdVideoAV1TileInfo',
        'structure': 'StdVideoAV1TileInfo',
        'is_string': False,
    },
    'pQuantization': {
        'type': CPointerType(CComplexType('StdVideoAV1Quantization')),
        'type_name': 'StdVideoAV1Quantization',
        'structure': 'StdVideoAV1Quantization',
        'is_string': False,
    },
    'pSegmentation': {
        'type': CPointerType(CComplexType('StdVideoAV1Segmentation')),
        'type_name': 'StdVideoAV1Segmentation',
        'structure': 'StdVideoAV1Segmentation',
        'is_string': False,
    },
    'pLoopFilter': {
        'type': CPointerType(CComplexType('StdVideoAV1LoopFilter')),
        'type_name': 'StdVideoAV1LoopFilter',
        'structure': 'StdVideoAV1LoopFilter',
        'is_string': False,
    },
    'pCDEF': {
        'type': CPointerType(CComplexType('StdVideoAV1CDEF')),
        'type_name': 'StdVideoAV1CDEF',
        'structure': 'StdVideoAV1CDEF',
        'is_string': False,
    },
    'pLoopRestoration': {
        'type': CPointerType(CComplexType('StdVideoAV1LoopRestoration')),
        'type_name': 'StdVideoAV1LoopRestoration',
        'structure': 'StdVideoAV1LoopRestoration',
        'is_string': False,
    },
    'pGlobalMotion': {
        'type': CPointerType(CComplexType('StdVideoAV1GlobalMotion')),
        'type_name': 'StdVideoAV1GlobalMotion',
        'structure': 'StdVideoAV1GlobalMotion',
        'is_string': False,
    },
    'pFilmGrain': {
        'type': CPointerType(CComplexType('StdVideoAV1FilmGrain')),
        'type_name': 'StdVideoAV1FilmGrain',
        'structure': 'StdVideoAV1FilmGrain',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1CDEF',
    'StdVideoAV1FilmGrain',
    'StdVideoAV1GlobalMotion',
    'StdVideoAV1LoopFilter',
    'StdVideoAV1LoopRestoration',
    'StdVideoAV1Quantization',
    'StdVideoAV1Segmentation',
    'StdVideoAV1TileInfo',
    'StdVideoDecodeAV1PictureInfoFlags',
}
_included_in_ = {
    'VkVideoDecodeAV1PictureInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
