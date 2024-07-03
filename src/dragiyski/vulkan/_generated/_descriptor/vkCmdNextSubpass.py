from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdNextSubpass'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'contents']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'contents': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
