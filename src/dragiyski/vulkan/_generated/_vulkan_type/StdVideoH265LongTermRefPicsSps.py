import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('used_by_curr_pic_lt_sps_flag', ctypes.c_uint32),
        ('lt_ref_pic_poc_lsb_sps', ctypes.ARRAY(ctypes.c_uint32, 32)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'used_by_curr_pic_lt_sps_flag': {'python_name': ['used', 'by', 'curr', 'pic', 'lt', 'sps', 'flag']},
        'lt_ref_pic_poc_lsb_sps': {'python_name': ['lt', 'ref', 'pic', 'poc', 'lsb', 'sps']},
    }
}
