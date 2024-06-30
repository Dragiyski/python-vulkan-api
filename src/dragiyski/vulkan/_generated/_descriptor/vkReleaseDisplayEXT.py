from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkReleaseDisplayEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'display']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'display': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = set()
