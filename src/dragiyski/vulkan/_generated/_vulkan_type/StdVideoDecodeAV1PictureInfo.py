import ctypes

class StdVideoDecodeAV1PictureInfo(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'flags': 'flags',
        'frame_type': 'frame_type',
        'current_frame_id': 'current_frame_id',
        'OrderHint': 'order_hint',
        'primary_ref_frame': 'primary_ref_frame',
        'refresh_frame_flags': 'refresh_frame_flags',
        'reserved1': 'reserved1',
        'interpolation_filter': 'interpolation_filter',
        'TxMode': 'tx_mode',
        'delta_q_res': 'delta_q_res',
        'delta_lf_res': 'delta_lf_res',
        'SkipModeFrame': 'skip_mode_frame',
        'coded_denom': 'coded_denom',
        'reserved2': 'reserved2',
        'OrderHints': 'order_hints',
        'expectedFrameId': 'expected_frame_id',
        'pTileInfo': 'tile_info',
        'pQuantization': 'quantization',
        'pSegmentation': 'segmentation',
        'pLoopFilter': 'loop_filter',
        'pCDEF': 'cdef',
        'pLoopRestoration': 'loop_restoration',
        'pGlobalMotion': 'global_motion',
        'pFilmGrain': 'film_grain',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std_decode',
    }
    _vk_enum_ = {
        'frame_type': 'StdVideoAV1FrameType',
        'interpolation_filter': 'StdVideoAV1InterpolationFilter',
        'TxMode': 'StdVideoAV1TxMode',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoAV1CDEF import StdVideoAV1CDEF
from .StdVideoAV1FilmGrain import StdVideoAV1FilmGrain
from .StdVideoAV1GlobalMotion import StdVideoAV1GlobalMotion
from .StdVideoAV1LoopFilter import StdVideoAV1LoopFilter
from .StdVideoAV1LoopRestoration import StdVideoAV1LoopRestoration
from .StdVideoAV1Quantization import StdVideoAV1Quantization
from .StdVideoAV1Segmentation import StdVideoAV1Segmentation
from .StdVideoAV1TileInfo import StdVideoAV1TileInfo
from .StdVideoDecodeAV1PictureInfoFlags import StdVideoDecodeAV1PictureInfoFlags

StdVideoDecodeAV1PictureInfo._fields_ = [
    ('flags', StdVideoDecodeAV1PictureInfoFlags),
    ('frame_type', ctypes.c_int),
    ('current_frame_id', ctypes.c_uint32),
    ('OrderHint', ctypes.c_uint8),
    ('primary_ref_frame', ctypes.c_uint8),
    ('refresh_frame_flags', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('interpolation_filter', ctypes.c_int),
    ('TxMode', ctypes.c_int),
    ('delta_q_res', ctypes.c_uint8),
    ('delta_lf_res', ctypes.c_uint8),
    ('SkipModeFrame', ctypes.ARRAY(ctypes.c_uint8, 2)),
    ('coded_denom', ctypes.c_uint8),
    ('reserved2', ctypes.ARRAY(ctypes.c_uint8, 3)),
    ('OrderHints', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ('expectedFrameId', ctypes.ARRAY(ctypes.c_uint32, 8)),
    ('pTileInfo', ctypes.POINTER(StdVideoAV1TileInfo)),
    ('pQuantization', ctypes.POINTER(StdVideoAV1Quantization)),
    ('pSegmentation', ctypes.POINTER(StdVideoAV1Segmentation)),
    ('pLoopFilter', ctypes.POINTER(StdVideoAV1LoopFilter)),
    ('pCDEF', ctypes.POINTER(StdVideoAV1CDEF)),
    ('pLoopRestoration', ctypes.POINTER(StdVideoAV1LoopRestoration)),
    ('pGlobalMotion', ctypes.POINTER(StdVideoAV1GlobalMotion)),
    ('pFilmGrain', ctypes.POINTER(StdVideoAV1FilmGrain)),
]

StdVideoDecodeAV1PictureInfo._type_ = {
    'flags': StdVideoDecodeAV1PictureInfoFlags,
    'frame_type': ctypes.c_int,
    'current_frame_id': ctypes.c_uint32,
    'OrderHint': ctypes.c_uint8,
    'primary_ref_frame': ctypes.c_uint8,
    'refresh_frame_flags': ctypes.c_uint8,
    'reserved1': ctypes.c_uint8,
    'interpolation_filter': ctypes.c_int,
    'TxMode': ctypes.c_int,
    'delta_q_res': ctypes.c_uint8,
    'delta_lf_res': ctypes.c_uint8,
    'SkipModeFrame': ctypes.ARRAY(ctypes.c_uint8, 2),
    'coded_denom': ctypes.c_uint8,
    'reserved2': ctypes.ARRAY(ctypes.c_uint8, 3),
    'OrderHints': ctypes.ARRAY(ctypes.c_uint8, 8),
    'expectedFrameId': ctypes.ARRAY(ctypes.c_uint32, 8),
    'pTileInfo': ctypes.POINTER(StdVideoAV1TileInfo),
    'pQuantization': ctypes.POINTER(StdVideoAV1Quantization),
    'pSegmentation': ctypes.POINTER(StdVideoAV1Segmentation),
    'pLoopFilter': ctypes.POINTER(StdVideoAV1LoopFilter),
    'pCDEF': ctypes.POINTER(StdVideoAV1CDEF),
    'pLoopRestoration': ctypes.POINTER(StdVideoAV1LoopRestoration),
    'pGlobalMotion': ctypes.POINTER(StdVideoAV1GlobalMotion),
    'pFilmGrain': ctypes.POINTER(StdVideoAV1FilmGrain),
}
