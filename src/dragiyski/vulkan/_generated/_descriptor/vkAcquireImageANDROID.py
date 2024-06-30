from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkAcquireImageANDROID'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'nativeFenceFd', 'semaphore', 'fence']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'nativeFenceFd': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'semaphore': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'fence': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = set()
_error_code_list_ = set()
