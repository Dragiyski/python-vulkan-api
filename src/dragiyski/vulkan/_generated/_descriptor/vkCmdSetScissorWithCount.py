from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetScissorWithCount'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'scissorCount', 'pScissors']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'scissorCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pScissors': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'is_string': False,
        'length': [['scissorCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
