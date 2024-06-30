from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDeferredOperationResultKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'operation']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'operation': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_NOT_READY'}
_error_code_list_ = set()
