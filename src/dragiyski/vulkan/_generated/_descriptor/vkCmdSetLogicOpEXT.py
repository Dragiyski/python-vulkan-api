from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdSetLogicOpEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'logicOp']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'logicOp': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
