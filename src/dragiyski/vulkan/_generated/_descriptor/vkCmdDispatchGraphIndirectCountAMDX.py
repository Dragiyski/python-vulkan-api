from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdDispatchGraphIndirectCountAMDX'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'scratch', 'countInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'scratch': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'countInfo': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
