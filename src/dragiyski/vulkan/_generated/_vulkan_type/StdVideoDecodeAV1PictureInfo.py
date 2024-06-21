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
