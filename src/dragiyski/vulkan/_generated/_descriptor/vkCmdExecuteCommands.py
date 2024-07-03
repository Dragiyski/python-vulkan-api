from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkCmdExecuteCommands'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'commandBufferCount', 'pCommandBuffers']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'commandBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pCommandBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['commandBufferCount']],
        'output': False,
    },
}
_return_type_ = CVoidType()
