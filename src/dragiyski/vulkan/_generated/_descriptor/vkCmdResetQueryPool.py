from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdResetQueryPool'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'queryPool', 'firstQuery', 'queryCount']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'queryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
