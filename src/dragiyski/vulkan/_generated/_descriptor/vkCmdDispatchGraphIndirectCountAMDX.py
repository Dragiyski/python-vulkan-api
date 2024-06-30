from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDispatchGraphIndirectCountAMDX'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'scratch', 'countInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'scratch': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'countInfo': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
