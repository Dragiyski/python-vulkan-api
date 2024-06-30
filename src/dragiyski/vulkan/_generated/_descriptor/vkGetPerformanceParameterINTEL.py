from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPerformanceParameterINTEL'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'parameter', 'pValue']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'parameter': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pValue': {
        'type': CPointerType(CComplexType('VkPerformanceValueINTEL')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_TOO_MANY_OBJECTS', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
