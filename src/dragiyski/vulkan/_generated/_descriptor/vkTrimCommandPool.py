from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkTrimCommandPool'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'commandPool', 'flags']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'commandPool': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
