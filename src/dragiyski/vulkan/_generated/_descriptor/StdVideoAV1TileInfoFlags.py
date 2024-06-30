from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1TileInfoFlags'
_member_list_ = ['uniform_tile_spacing_flag', 'reserved']
_member_info_ = {
    'uniform_tile_spacing_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 31,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoAV1TileInfo',
}
_input_of_ = set()
_output_of_ = set()
