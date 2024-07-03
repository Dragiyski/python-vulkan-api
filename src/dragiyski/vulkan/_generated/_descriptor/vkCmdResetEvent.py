from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdResetEvent'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'event', 'stageMask']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'event': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'stageMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
