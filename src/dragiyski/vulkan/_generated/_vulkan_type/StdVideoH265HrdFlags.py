import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('nal_hrd_parameters_present_flag', ctypes.c_uint32, 1),
        ('vcl_hrd_parameters_present_flag', ctypes.c_uint32, 1),
        ('sub_pic_hrd_params_present_flag', ctypes.c_uint32, 1),
        ('sub_pic_cpb_params_in_pic_timing_sei_flag', ctypes.c_uint32, 1),
        ('fixed_pic_rate_general_flag', ctypes.c_uint32, 8),
        ('fixed_pic_rate_within_cvs_flag', ctypes.c_uint32, 8),
        ('low_delay_hrd_flag', ctypes.c_uint32, 8),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265HrdParameters',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'nal_hrd_parameters_present_flag': {'python_name': ['nal', 'hrd', 'parameters', 'present', 'flag']},
        'vcl_hrd_parameters_present_flag': {'python_name': ['vcl', 'hrd', 'parameters', 'present', 'flag']},
        'sub_pic_hrd_params_present_flag': {'python_name': ['sub', 'pic', 'hrd', 'params', 'present', 'flag']},
        'sub_pic_cpb_params_in_pic_timing_sei_flag': {'python_name': ['sub', 'pic', 'cpb', 'params', 'in', 'pic', 'timing', 'sei', 'flag']},
        'fixed_pic_rate_general_flag': {'python_name': ['fixed', 'pic', 'rate', 'general', 'flag']},
        'fixed_pic_rate_within_cvs_flag': {'python_name': ['fixed', 'pic', 'rate', 'within', 'cvs', 'flag']},
        'low_delay_hrd_flag': {'python_name': ['low', 'delay', 'hrd', 'flag']},
    }
}
