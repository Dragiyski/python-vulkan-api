import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1CDEF import CType as StdVideoAV1CDEF
from .StdVideoAV1FilmGrain import CType as StdVideoAV1FilmGrain
from .StdVideoAV1GlobalMotion import CType as StdVideoAV1GlobalMotion
from .StdVideoAV1LoopFilter import CType as StdVideoAV1LoopFilter
from .StdVideoAV1LoopRestoration import CType as StdVideoAV1LoopRestoration
from .StdVideoAV1Quantization import CType as StdVideoAV1Quantization
from .StdVideoAV1Segmentation import CType as StdVideoAV1Segmentation
from .StdVideoAV1TileInfo import CType as StdVideoAV1TileInfo
from .StdVideoDecodeAV1PictureInfoFlags import CType as StdVideoDecodeAV1PictureInfoFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1CDEF',
        'StdVideoAV1FilmGrain',
        'StdVideoAV1GlobalMotion',
        'StdVideoAV1LoopFilter',
        'StdVideoAV1LoopRestoration',
        'StdVideoAV1Quantization',
        'StdVideoAV1Segmentation',
        'StdVideoAV1TileInfo',
        'StdVideoDecodeAV1PictureInfoFlags',
    },
    'included_in': {
        'VkVideoDecodeAV1PictureInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoDecodeAV1PictureInfoFlags'},
        'frame_type': {'python_name': ['frame', 'type'], 'type': 'StdVideoAV1FrameType'},
        'current_frame_id': {'python_name': ['current', 'frame', 'id']},
        'OrderHint': {'python_name': ['order', 'hint']},
        'primary_ref_frame': {'python_name': ['primary', 'ref', 'frame']},
        'refresh_frame_flags': {'python_name': ['refresh', 'frame', 'flags']},
        'reserved1': {'python_name': ['reserved1']},
        'interpolation_filter': {'python_name': ['interpolation', 'filter'], 'type': 'StdVideoAV1InterpolationFilter'},
        'TxMode': {'python_name': ['tx', 'mode'], 'type': 'StdVideoAV1TxMode'},
        'delta_q_res': {'python_name': ['delta', 'q', 'res']},
        'delta_lf_res': {'python_name': ['delta', 'lf', 'res']},
        'SkipModeFrame': {'python_name': ['skip', 'mode', 'frame']},
        'coded_denom': {'python_name': ['coded', 'denom']},
        'reserved2': {'python_name': ['reserved2']},
        'OrderHints': {'python_name': ['order', 'hints']},
        'expectedFrameId': {'python_name': ['expected', 'frame', 'id']},
        'pTileInfo': {'python_name': ['p', 'tile', 'info'], 'type': 'StdVideoAV1TileInfo'},
        'pQuantization': {'python_name': ['p', 'quantization'], 'type': 'StdVideoAV1Quantization'},
        'pSegmentation': {'python_name': ['p', 'segmentation'], 'type': 'StdVideoAV1Segmentation'},
        'pLoopFilter': {'python_name': ['p', 'loop', 'filter'], 'type': 'StdVideoAV1LoopFilter'},
        'pCDEF': {'python_name': ['p', 'cdef'], 'type': 'StdVideoAV1CDEF'},
        'pLoopRestoration': {'python_name': ['p', 'loop', 'restoration'], 'type': 'StdVideoAV1LoopRestoration'},
        'pGlobalMotion': {'python_name': ['p', 'global', 'motion'], 'type': 'StdVideoAV1GlobalMotion'},
        'pFilmGrain': {'python_name': ['p', 'film', 'grain'], 'type': 'StdVideoAV1FilmGrain'},
    }
}
