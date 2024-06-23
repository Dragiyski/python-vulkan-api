import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265HrdFlags import CType as StdVideoH265HrdFlags
from .StdVideoH265SubLayerHrdParameters import CType as StdVideoH265SubLayerHrdParameters

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH265HrdFlags',
        'StdVideoH265SubLayerHrdParameters',
    },
    'included_in': {
        'StdVideoH265SequenceParameterSetVui',
        'StdVideoH265VideoParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH265HrdFlags'},
        'tick_divisor_minus2': {'python_name': ['tick', 'divisor', 'minus2']},
        'du_cpb_removal_delay_increment_length_minus1': {'python_name': ['du', 'cpb', 'removal', 'delay', 'increment', 'length', 'minus1']},
        'dpb_output_delay_du_length_minus1': {'python_name': ['dpb', 'output', 'delay', 'du', 'length', 'minus1']},
        'bit_rate_scale': {'python_name': ['bit', 'rate', 'scale']},
        'cpb_size_scale': {'python_name': ['cpb', 'size', 'scale']},
        'cpb_size_du_scale': {'python_name': ['cpb', 'size', 'du', 'scale']},
        'initial_cpb_removal_delay_length_minus1': {'python_name': ['initial', 'cpb', 'removal', 'delay', 'length', 'minus1']},
        'au_cpb_removal_delay_length_minus1': {'python_name': ['au', 'cpb', 'removal', 'delay', 'length', 'minus1']},
        'dpb_output_delay_length_minus1': {'python_name': ['dpb', 'output', 'delay', 'length', 'minus1']},
        'cpb_cnt_minus1': {'python_name': ['cpb', 'cnt', 'minus1']},
        'elemental_duration_in_tc_minus1': {'python_name': ['elemental', 'duration', 'in', 'tc', 'minus1']},
        'reserved': {'python_name': ['reserved']},
        'pSubLayerHrdParametersNal': {'python_name': ['p', 'sub', 'layer', 'hrd', 'parameters', 'nal'], 'type': 'StdVideoH265SubLayerHrdParameters'},
        'pSubLayerHrdParametersVcl': {'python_name': ['p', 'sub', 'layer', 'hrd', 'parameters', 'vcl'], 'type': 'StdVideoH265SubLayerHrdParameters'},
    }
}
