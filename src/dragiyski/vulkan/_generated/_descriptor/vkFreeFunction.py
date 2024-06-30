from ..._ctypes import *

_category_ = 'callback'
_name_ = 'vkFreeFunction'
_constructor_ = 'VKAPI_PTR'
_argument_list_ = ['pUserData', 'pMemory']
_argument_info_ = {
    'pUserData': {
        'type': CIntType('c_void_p'),
    },
    'pMemory': {
        'type': CIntType('c_void_p'),
    },
}
_return_type_ = CVoidType()
