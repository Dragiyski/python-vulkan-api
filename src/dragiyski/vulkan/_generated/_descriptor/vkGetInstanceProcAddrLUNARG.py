from ..._ctypes import *

_category_ = 'callback'
_name_ = 'vkGetInstanceProcAddrLUNARG'
_constructor_ = 'VKAPI_PTR'
_argument_list_ = ['instance', 'pName']
_argument_info_ = {
    'instance': {
        'type': CIntType('c_void_p'),
    },
    'pName': {
        'type': CStringType('c_char_p'),
    },
}
_return_type_ = CFunctionType('vkVoidFunction')
