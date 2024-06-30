from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDrmDisplayEXT'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'drmFd', 'connectorId', 'display']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'drmFd': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'connectorId': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'display': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
