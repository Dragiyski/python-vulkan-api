from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkFreeCommandBuffers'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'commandPool', 'commandBufferCount', 'pCommandBuffers']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'commandPool': {
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
