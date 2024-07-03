from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetFenceWin32HandleKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pGetWin32HandleInfo', 'pHandle']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pGetWin32HandleInfo': {
        'type': CPointerType(CComplexType('VkFenceGetWin32HandleInfoKHR')),
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
