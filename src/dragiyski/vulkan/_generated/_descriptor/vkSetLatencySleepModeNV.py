from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkSetLatencySleepModeNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'pSleepModeInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSleepModeInfo': {
        'type': CPointerType(CComplexType('VkLatencySleepModeInfoNV')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INITIALIZATION_FAILED'}
