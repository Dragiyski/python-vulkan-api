from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdResetEvent2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'event', 'stageMask']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'event': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stageMask': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
