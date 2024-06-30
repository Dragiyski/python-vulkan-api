from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkWaitForPresentKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'presentId', 'timeout']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'presentId': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'timeout': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_TIMEOUT', 'VK_SUBOPTIMAL_KHR'}
_error_code_list_ = {'VK_ERROR_DEVICE_LOST', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DATE_KHR', 'VK_ERROR_FULL_SCREEN_EXCLUSIVE_MODE_LOST_EXT', 'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
