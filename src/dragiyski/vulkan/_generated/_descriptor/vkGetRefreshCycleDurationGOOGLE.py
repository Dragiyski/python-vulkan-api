from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetRefreshCycleDurationGOOGLE'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'pDisplayTimingProperties']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDisplayTimingProperties': {
        'type': CPointerType(CComplexType('VkRefreshCycleDurationGOOGLE')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_DEVICE_LOST', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
