from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetBlendConstants'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'blendConstants']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'blendConstants': {
        'type': CArrayType(CFloatType('c_float'), 4),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
