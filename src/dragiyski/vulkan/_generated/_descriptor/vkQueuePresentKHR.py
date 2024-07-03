from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkQueuePresentKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['queue', 'pPresentInfo']
_argument_info_ = {
    'queue': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pPresentInfo': {
        'type': CPointerType(CComplexType('VkPresentInfoKHR')),
        'is_string': False,
        'output': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_SUBOPTIMAL_KHR'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_FULL_SCREEN_EXCLUSIVE_MODE_LOST_EXT', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_DEVICE_LOST', 'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_OUT_OF_DATE_KHR'}
