from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkCmdExecuteCommands'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['commandBuffer', 'commandBufferCount', 'pCommandBuffers']
_argument_info_ = {
    'commandBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'commandBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCommandBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['commandBufferCount']],
    },
}
_return_type_ = CVoidType()
