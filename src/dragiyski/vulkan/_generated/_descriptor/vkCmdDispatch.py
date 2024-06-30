from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDispatch'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'groupCountX', 'groupCountY', 'groupCountZ']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'groupCountX': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'groupCountY': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'groupCountZ': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
