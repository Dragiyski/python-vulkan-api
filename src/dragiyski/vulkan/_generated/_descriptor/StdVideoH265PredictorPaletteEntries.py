from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265PredictorPaletteEntries'
_member_list_ = ['PredictorPaletteEntries']
_member_info_ = {
    'PredictorPaletteEntries': {
        'type': CArrayType(CArrayType(CIntType('c_uint16'), 128), 3),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265PictureParameterSet',
    'StdVideoH265SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
