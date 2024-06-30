from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkFreeCommandBuffers'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'commandPool', 'commandBufferCount', 'pCommandBuffers']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'commandPool': {
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
