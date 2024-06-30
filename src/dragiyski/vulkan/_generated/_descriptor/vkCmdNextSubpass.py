from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdNextSubpass'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'contents']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'contents': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
