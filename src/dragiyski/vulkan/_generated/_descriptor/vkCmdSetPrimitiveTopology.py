from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetPrimitiveTopology'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'primitiveTopology']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'primitiveTopology': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
