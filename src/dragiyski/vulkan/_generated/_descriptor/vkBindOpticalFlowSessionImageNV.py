from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkBindOpticalFlowSessionImageNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'session', 'bindingPoint', 'view', 'layout']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'session': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'bindingPoint': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'view': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'layout': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_INITIALIZATION_FAILED'}
