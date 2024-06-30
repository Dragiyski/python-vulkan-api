from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkMapMemory'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'memory', 'offset', 'size', 'flags', 'ppData']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'ppData': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_MEMORY_MAP_FAILED', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
