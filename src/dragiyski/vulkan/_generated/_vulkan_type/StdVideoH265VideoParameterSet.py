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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH265DecPicBufMgr',
        'StdVideoH265HrdParameters',
        'StdVideoH265ProfileTierLevel',
        'StdVideoH265VpsFlags',
    },
    'included_in': {
        'VkVideoDecodeH265SessionParametersAddInfoKHR',
        'VkVideoEncodeH265SessionParametersAddInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH265VpsFlags'},
        'vps_video_parameter_set_id': {'python_name': ['vps', 'video', 'parameter', 'set', 'id']},
        'vps_max_sub_layers_minus1': {'python_name': ['vps', 'max', 'sub', 'layers', 'minus1']},
        'reserved1': {'python_name': ['reserved1']},
        'reserved2': {'python_name': ['reserved2']},
        'vps_num_units_in_tick': {'python_name': ['vps', 'num', 'units', 'in', 'tick']},
        'vps_time_scale': {'python_name': ['vps', 'time', 'scale']},
        'vps_num_ticks_poc_diff_one_minus1': {'python_name': ['vps', 'num', 'ticks', 'poc', 'diff', 'one', 'minus1']},
        'reserved3': {'python_name': ['reserved3']},
        'pDecPicBufMgr': {'python_name': ['p', 'dec', 'pic', 'buf', 'mgr'], 'type': 'StdVideoH265DecPicBufMgr'},
        'pHrdParameters': {'python_name': ['p', 'hrd', 'parameters'], 'type': 'StdVideoH265HrdParameters'},
        'pProfileTierLevel': {'python_name': ['p', 'profile', 'tier', 'level'], 'type': 'StdVideoH265ProfileTierLevel'},
    }
}
