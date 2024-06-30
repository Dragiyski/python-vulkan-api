from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkBindOpticalFlowSessionImageNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'session', 'bindingPoint', 'view', 'layout']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'session': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'bindingPoint': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'view': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
