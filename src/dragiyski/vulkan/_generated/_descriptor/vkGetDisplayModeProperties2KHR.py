from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDisplayModeProperties2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'display', 'pPropertyCount', 'pProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'display': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pProperties': {
        'type': CPointerType(CComplexType('VkDisplayModeProperties2KHR')),
        'is_string': False,
        'length': [['pPropertyCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
