from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkAcquireNextImage2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pAcquireInfo', 'pImageIndex']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pAcquireInfo': {
        'type': CPointerType(CComplexType('VkAcquireNextImageInfoKHR')),
        'is_string': False,
        'output': False,
    },
    'pImageIndex': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_NOT_READY', 'VK_SUCCESS', 'VK_SUBOPTIMAL_KHR', 'VK_TIMEOUT'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_FULL_SCREEN_EXCLUSIVE_MODE_LOST_EXT', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_DEVICE_LOST', 'VK_ERROR_SURFACE_LOST_KHR', 'VK_ERROR_OUT_OF_DATE_KHR'}
