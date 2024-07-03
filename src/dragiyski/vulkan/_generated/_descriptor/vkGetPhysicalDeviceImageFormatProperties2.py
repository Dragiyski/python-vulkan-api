from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceImageFormatProperties2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pImageFormatInfo', 'pImageFormatProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pImageFormatInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceImageFormatInfo2')),
        'is_string': False,
        'output': False,
    },
    'pImageFormatProperties': {
        'type': CPointerType(CComplexType('VkImageFormatProperties2')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_VIDEO_PROFILE_FORMAT_NOT_SUPPORTED_KHR', 'VK_ERROR_FORMAT_NOT_SUPPORTED', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_VIDEO_PROFILE_OPERATION_NOT_SUPPORTED_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_IMAGE_USAGE_NOT_SUPPORTED_KHR', 'VK_ERROR_VIDEO_PICTURE_LAYOUT_NOT_SUPPORTED_KHR', 'VK_ERROR_VIDEO_PROFILE_CODEC_NOT_SUPPORTED_KHR'}
