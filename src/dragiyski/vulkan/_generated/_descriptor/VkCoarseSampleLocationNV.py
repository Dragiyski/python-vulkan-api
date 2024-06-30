from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCoarseSampleLocationNV'
_member_list_ = ['pixelX', 'pixelY', 'sample']
_member_info_ = {
    'pixelX': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pixelY': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sample': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkCoarseSampleOrderCustomNV',
}
_input_of_ = set()
_output_of_ = set()
