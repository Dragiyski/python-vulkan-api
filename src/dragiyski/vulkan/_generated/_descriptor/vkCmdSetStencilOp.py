from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetStencilOp'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'faceMask', 'failOp', 'passOp', 'depthFailOp', 'compareOp']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'faceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'failOp': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'passOp': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'depthFailOp': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'compareOp': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
