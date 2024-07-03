from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetMemoryWin32HandleNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'memory', 'handleType', 'pHandle']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pHandle': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_TOO_MANY_OBJECTS'}
