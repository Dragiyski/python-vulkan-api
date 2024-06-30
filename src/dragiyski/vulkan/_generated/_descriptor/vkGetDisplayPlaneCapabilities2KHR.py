from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDisplayPlaneCapabilities2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pDisplayPlaneInfo', 'pCapabilities']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pDisplayPlaneInfo': {
        'type': CPointerType(CComplexType('VkDisplayPlaneInfo2KHR')),
        'is_string': False,
    },
    'pCapabilities': {
        'type': CPointerType(CComplexType('VkDisplayPlaneCapabilities2KHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
