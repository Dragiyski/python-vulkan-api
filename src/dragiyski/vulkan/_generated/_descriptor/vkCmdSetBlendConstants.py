from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetBlendConstants'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'blendConstants']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'blendConstants': {
        'type': CArrayType(CFloatType('c_float'), 4),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
