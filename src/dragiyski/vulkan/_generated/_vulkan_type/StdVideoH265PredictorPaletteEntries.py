import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('PredictorPaletteEntries', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint16, 128), 3)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265PictureParameterSet',
        'StdVideoH265SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'PredictorPaletteEntries': {'python_name': ['predictor', 'palette', 'entries']},
    }
}
