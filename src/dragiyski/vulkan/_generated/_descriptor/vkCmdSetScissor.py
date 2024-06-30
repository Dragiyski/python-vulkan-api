from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdSetScissor'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'firstScissor', 'scissorCount', 'pScissors']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstScissor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'scissorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pScissors': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'is_string': False,
        'length': [['scissorCount']],
    },
}
_return_type_ = CVoidType()
