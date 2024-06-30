from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkIndirectCommandsStreamNV'
_member_list_ = ['buffer', 'offset']
_member_info_ = {
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkGeneratedCommandsInfoNV',
}
_input_of_ = set()
_output_of_ = set()
