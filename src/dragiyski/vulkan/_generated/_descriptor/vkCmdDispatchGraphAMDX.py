from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdDispatchGraphAMDX'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'scratch', 'pCountInfo']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'scratch': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'pCountInfo': {
        'type': CPointerType(CComplexType('VkDispatchGraphCountInfoAMDX')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
