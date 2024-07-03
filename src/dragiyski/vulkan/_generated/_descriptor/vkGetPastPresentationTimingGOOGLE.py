from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPastPresentationTimingGOOGLE'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'swapchain', 'pPresentationTimingCount', 'pPresentationTimings']
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
    'pPresentationTimingCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pPresentationTimings': {
        'type': CPointerType(CComplexType('VkPastPresentationTimingGOOGLE')),
        'is_string': False,
        'length': [['pPresentationTimingCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_OUT_OF_DATE_KHR', 'VK_ERROR_DEVICE_LOST'}
