from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetMemoryWin32HandlePropertiesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'handleType', 'handle', 'pMemoryWin32HandleProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'handle': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMemoryWin32HandleProperties': {
        'type': CPointerType(CComplexType('VkMemoryWin32HandlePropertiesKHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_EXTERNAL_HANDLE', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
