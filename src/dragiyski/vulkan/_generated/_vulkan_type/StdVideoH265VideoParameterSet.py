import ctypes

class StdVideoH265VideoParameterSet(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoH265VpsFlags,
            'vps_video_parameter_set_id': ctypes.c_uint8,
            'vps_max_sub_layers_minus1': ctypes.c_uint8,
            'reserved1': ctypes.c_uint8,
            'reserved2': ctypes.c_uint8,
            'vps_num_units_in_tick': ctypes.c_uint32,
            'vps_time_scale': ctypes.c_uint32,
            'vps_num_ticks_poc_diff_one_minus1': ctypes.c_uint32,
            'reserved3': ctypes.c_uint32,
            'pDecPicBufMgr': ctypes.POINTER(StdVideoH265DecPicBufMgr),
            'pHrdParameters': ctypes.POINTER(StdVideoH265HrdParameters),
            'pProfileTierLevel': ctypes.POINTER(StdVideoH265ProfileTierLevel),
        }


from .StdVideoH265DecPicBufMgr import StdVideoH265DecPicBufMgr
from .StdVideoH265HrdParameters import StdVideoH265HrdParameters
from .StdVideoH265ProfileTierLevel import StdVideoH265ProfileTierLevel
from .StdVideoH265VpsFlags import StdVideoH265VpsFlags

StdVideoH265VideoParameterSet._fields_ = [
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
