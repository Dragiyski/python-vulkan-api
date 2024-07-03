from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceProcAddr'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pName']
_argument_info_ = {
    'device': {
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
