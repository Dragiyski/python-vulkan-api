from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceVideoCapabilitiesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pVideoProfile', 'pCapabilities']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pVideoProfile': {
        'type': CPointerType(CComplexType('VkVideoProfileInfoKHR')),
        'is_string': False,
    },
    'pCapabilities': {
        'type': CPointerType(CComplexType('VkVideoCapabilitiesKHR')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_VIDEO_PROFILE_CODEC_NOT_SUPPORTED_KHR', 'VK_ERROR_VIDEO_PICTURE_LAYOUT_NOT_SUPPORTED_KHR', 'VK_ERROR_VIDEO_PROFILE_OPERATION_NOT_SUPPORTED_KHR', 'VK_ERROR_VIDEO_PROFILE_FORMAT_NOT_SUPPORTED_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
