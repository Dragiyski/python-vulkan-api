from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetInstanceProcAddr'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pName']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pName': {
        'type': CStringType('c_char_p'),
        'is_string': True,
        'length': [],
    },
}
_return_type_ = CFunctionType('vkVoidFunction')
