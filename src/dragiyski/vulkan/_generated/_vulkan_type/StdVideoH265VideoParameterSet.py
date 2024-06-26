import ctypes

class StdVideoH265VideoParameterSet(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH265DecPicBufMgr',
        'StdVideoH265HrdParameters',
        'StdVideoH265ProfileTierLevel',
        'StdVideoH265VpsFlags',
    }
    _included_in_ = {
        'VkVideoDecodeH265SessionParametersAddInfoKHR',
        'VkVideoEncodeH265SessionParametersAddInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'vps_video_parameter_set_id': 'vps_video_parameter_set_id',
        'vps_max_sub_layers_minus1': 'vps_max_sub_layers_minus1',
        'reserved1': 'reserved1',
        'reserved2': 'reserved2',
        'vps_num_units_in_tick': 'vps_num_units_in_tick',
        'vps_time_scale': 'vps_time_scale',
        'vps_num_ticks_poc_diff_one_minus1': 'vps_num_ticks_poc_diff_one_minus1',
        'reserved3': 'reserved3',
        'pDecPicBufMgr': 'dec_pic_buf_mgr',
        'pHrdParameters': 'hrd_parameters',
        'pProfileTierLevel': 'profile_tier_level',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


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

StdVideoH265VideoParameterSet._type_ = {
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
