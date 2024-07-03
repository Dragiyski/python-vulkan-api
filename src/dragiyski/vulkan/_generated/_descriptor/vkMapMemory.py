from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkMapMemory'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'memory', 'offset', 'size', 'flags', 'ppData']
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
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
        'output': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'ppData': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_MEMORY_MAP_FAILED', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
