from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdResetQueryPool'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'queryPool', 'firstQuery', 'queryCount']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'queryPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstQuery': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'queryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
