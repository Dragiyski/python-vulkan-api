from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkLatencySleepNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'pSleepInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pSleepInfo': {
        'type': CPointerType(CComplexType('VkLatencySleepInfoNV')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = set()
