import ctypes

class StdVideoH265HrdParameters(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoH265HrdFlags,
            'tick_divisor_minus2': ctypes.c_uint8,
            'du_cpb_removal_delay_increment_length_minus1': ctypes.c_uint8,
            'dpb_output_delay_du_length_minus1': ctypes.c_uint8,
            'bit_rate_scale': ctypes.c_uint8,
            'cpb_size_scale': ctypes.c_uint8,
            'cpb_size_du_scale': ctypes.c_uint8,
            'initial_cpb_removal_delay_length_minus1': ctypes.c_uint8,
            'au_cpb_removal_delay_length_minus1': ctypes.c_uint8,
            'dpb_output_delay_length_minus1': ctypes.c_uint8,
            'cpb_cnt_minus1': ctypes.ARRAY(ctypes.c_uint8, 7),
            'elemental_duration_in_tc_minus1': ctypes.ARRAY(ctypes.c_uint16, 7),
            'reserved': ctypes.ARRAY(ctypes.c_uint16, 3),
            'pSubLayerHrdParametersNal': ctypes.POINTER(StdVideoH265SubLayerHrdParameters),
            'pSubLayerHrdParametersVcl': ctypes.POINTER(StdVideoH265SubLayerHrdParameters),
        }


from .StdVideoH265HrdFlags import StdVideoH265HrdFlags
from .StdVideoH265SubLayerHrdParameters import StdVideoH265SubLayerHrdParameters

StdVideoH265HrdParameters._fields_ = [
    ('flags', StdVideoH265HrdFlags),
    ('tick_divisor_minus2', ctypes.c_uint8),
    ('du_cpb_removal_delay_increment_length_minus1', ctypes.c_uint8),
    ('dpb_output_delay_du_length_minus1', ctypes.c_uint8),
    ('bit_rate_scale', ctypes.c_uint8),
    ('cpb_size_scale', ctypes.c_uint8),
    ('cpb_size_du_scale', ctypes.c_uint8),
    ('initial_cpb_removal_delay_length_minus1', ctypes.c_uint8),
    ('au_cpb_removal_delay_length_minus1', ctypes.c_uint8),
    ('dpb_output_delay_length_minus1', ctypes.c_uint8),
    ('cpb_cnt_minus1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('elemental_duration_in_tc_minus1', ctypes.ARRAY(ctypes.c_uint16, 7)),
    ('reserved', ctypes.ARRAY(ctypes.c_uint16, 3)),
    ('pSubLayerHrdParametersNal', ctypes.POINTER(StdVideoH265SubLayerHrdParameters)),
    ('pSubLayerHrdParametersVcl', ctypes.POINTER(StdVideoH265SubLayerHrdParameters)),
]
