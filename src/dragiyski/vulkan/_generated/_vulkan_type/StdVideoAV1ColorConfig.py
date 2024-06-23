import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1ColorConfigFlags import CType as StdVideoAV1ColorConfigFlags

CType._fields_ = [
    ('flags', StdVideoAV1ColorConfigFlags),
    ('BitDepth', ctypes.c_uint8),
    ('subsampling_x', ctypes.c_uint8),
    ('subsampling_y', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('color_primaries', ctypes.c_int),
    ('transfer_characteristics', ctypes.c_int),
    ('matrix_coefficients', ctypes.c_int),
    ('chroma_sample_position', ctypes.c_int),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1ColorConfigFlags',
    },
    'included_in': {
        'StdVideoAV1SequenceHeader',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoAV1ColorConfigFlags'},
        'BitDepth': {'python_name': ['bit', 'depth']},
        'subsampling_x': {'python_name': ['subsampling', 'x']},
        'subsampling_y': {'python_name': ['subsampling', 'y']},
        'reserved1': {'python_name': ['reserved1']},
        'color_primaries': {'python_name': ['color', 'primaries'], 'type': 'StdVideoAV1ColorPrimaries'},
        'transfer_characteristics': {'python_name': ['transfer', 'characteristics'], 'type': 'StdVideoAV1TransferCharacteristics'},
        'matrix_coefficients': {'python_name': ['matrix', 'coefficients'], 'type': 'StdVideoAV1MatrixCoefficients'},
        'chroma_sample_position': {'python_name': ['chroma', 'sample', 'position'], 'type': 'StdVideoAV1ChromaSamplePosition'},
    }
}
