from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetExclusiveScissorNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstExclusiveScissor', 'exclusiveScissorCount', 'pExclusiveScissors']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'firstExclusiveScissor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'exclusiveScissorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pExclusiveScissors': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'is_string': False,
        'length': [['exclusiveScissorCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
