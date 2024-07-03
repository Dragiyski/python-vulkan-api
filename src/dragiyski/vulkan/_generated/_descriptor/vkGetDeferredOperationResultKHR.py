from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeferredOperationResultKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'operation']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'operation': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_NOT_READY', 'VK_SUCCESS'}
_error_code_list_ = set()
