from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetStencilOp'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'faceMask', 'failOp', 'passOp', 'depthFailOp', 'compareOp']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'faceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'failOp': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'passOp': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'depthFailOp': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'compareOp': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
