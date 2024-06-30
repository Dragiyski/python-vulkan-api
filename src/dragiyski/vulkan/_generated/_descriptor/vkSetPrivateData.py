from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkSetPrivateData'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'objectType', 'objectHandle', 'privateDataSlot', 'data']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'objectType': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'objectHandle': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'privateDataSlot': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'data': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY'}
