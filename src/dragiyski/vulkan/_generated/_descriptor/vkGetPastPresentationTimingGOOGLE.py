from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPastPresentationTimingGOOGLE'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'pPresentationTimingCount', 'pPresentationTimings']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pPresentationTimingCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
    'pPresentationTimings': {
        'type': CPointerType(CComplexType('VkPastPresentationTimingGOOGLE')),
        'is_string': False,
        'length': [['pPresentationTimingCount']],
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_DEVICE_LOST', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DATE_KHR'}
