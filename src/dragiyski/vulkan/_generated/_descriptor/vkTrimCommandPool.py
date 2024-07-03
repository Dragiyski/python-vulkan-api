from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkTrimCommandPool'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'commandPool', 'flags']
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
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CVoidType()
