from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkWaitForFences'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'fenceCount', 'pFences', 'waitAll', 'timeout']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'fenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pFences': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'length': [['fenceCount']],
        'output': False,
    },
    'waitAll': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'timeout': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_TIMEOUT'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_DEVICE_LOST'}
