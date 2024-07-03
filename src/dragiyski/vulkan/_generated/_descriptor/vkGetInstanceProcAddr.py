from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetInstanceProcAddr'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['instance', 'pName']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pName': {
        'type': CStringType('c_char_p'),
        'is_string': True,
        'length': [],
        'output': False,
    },
}
_return_type_ = CFunctionType('vkVoidFunction')
