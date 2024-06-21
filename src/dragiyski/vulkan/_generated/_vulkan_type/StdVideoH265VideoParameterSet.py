import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265DecPicBufMgr import CType as StdVideoH265DecPicBufMgr
from .StdVideoH265HrdParameters import CType as StdVideoH265HrdParameters
from .StdVideoH265ProfileTierLevel import CType as StdVideoH265ProfileTierLevel
from .StdVideoH265VpsFlags import CType as StdVideoH265VpsFlags

CType._fields_ = [
    ('flags', StdVideoH265VpsFlags),
    ('vps_video_parameter_set_id', ctypes.c_uint8),
    ('vps_max_sub_layers_minus1', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('reserved2', ctypes.c_uint8),
    ('vps_num_units_in_tick', ctypes.c_uint32),
    ('vps_time_scale', ctypes.c_uint32),
    ('vps_num_ticks_poc_diff_one_minus1', ctypes.c_uint32),
    ('reserved3', ctypes.c_uint32),
    ('pDecPicBufMgr', ctypes.POINTER(StdVideoH265DecPicBufMgr)),
    ('pHrdParameters', ctypes.POINTER(StdVideoH265HrdParameters)),
    ('pProfileTierLevel', ctypes.POINTER(StdVideoH265ProfileTierLevel)),
]
