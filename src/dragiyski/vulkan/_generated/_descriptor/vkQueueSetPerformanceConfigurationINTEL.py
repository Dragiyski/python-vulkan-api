from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkQueueSetPerformanceConfigurationINTEL'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'configuration']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'configuration': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_TOO_MANY_OBJECTS'}
