from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkUpdateVideoSessionParametersKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'videoSessionParameters', 'pUpdateInfo']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoSessionParameters': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pUpdateInfo': {
        'type': CPointerType(CComplexType('VkVideoSessionParametersUpdateInfoKHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_INVALID_VIDEO_STD_PARAMETERS_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY'}
