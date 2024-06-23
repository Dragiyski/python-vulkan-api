import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('vps_temporal_id_nesting_flag', ctypes.c_uint32, 1),
        ('vps_sub_layer_ordering_info_present_flag', ctypes.c_uint32, 1),
        ('vps_timing_info_present_flag', ctypes.c_uint32, 1),
        ('vps_poc_proportional_to_timing_flag', ctypes.c_uint32, 1),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265VideoParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'vps_temporal_id_nesting_flag': {'python_name': ['vps', 'temporal', 'id', 'nesting', 'flag']},
        'vps_sub_layer_ordering_info_present_flag': {'python_name': ['vps', 'sub', 'layer', 'ordering', 'info', 'present', 'flag']},
        'vps_timing_info_present_flag': {'python_name': ['vps', 'timing', 'info', 'present', 'flag']},
        'vps_poc_proportional_to_timing_flag': {'python_name': ['vps', 'poc', 'proportional', 'to', 'timing', 'flag']},
    }
}
