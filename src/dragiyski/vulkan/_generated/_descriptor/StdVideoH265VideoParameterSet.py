from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265VideoParameterSet'
_member_list_ = ['flags', 'vps_video_parameter_set_id', 'vps_max_sub_layers_minus1', 'reserved1', 'reserved2', 'vps_num_units_in_tick', 'vps_time_scale', 'vps_num_ticks_poc_diff_one_minus1', 'reserved3', 'pDecPicBufMgr', 'pHrdParameters', 'pProfileTierLevel']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH265VpsFlags'),
        'type_name': 'StdVideoH265VpsFlags',
        'structure': 'StdVideoH265VpsFlags',
        'is_string': False,
    },
    'vps_video_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'vps_max_sub_layers_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'vps_num_units_in_tick': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vps_time_scale': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vps_num_ticks_poc_diff_one_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'reserved3': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDecPicBufMgr': {
        'type': CPointerType(CComplexType('StdVideoH265DecPicBufMgr')),
        'type_name': 'StdVideoH265DecPicBufMgr',
        'structure': 'StdVideoH265DecPicBufMgr',
        'is_string': False,
    },
    'pHrdParameters': {
        'type': CPointerType(CComplexType('StdVideoH265HrdParameters')),
        'type_name': 'StdVideoH265HrdParameters',
        'structure': 'StdVideoH265HrdParameters',
        'is_string': False,
    },
    'pProfileTierLevel': {
        'type': CPointerType(CComplexType('StdVideoH265ProfileTierLevel')),
        'type_name': 'StdVideoH265ProfileTierLevel',
        'structure': 'StdVideoH265ProfileTierLevel',
        'is_string': False,
    },
}
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
