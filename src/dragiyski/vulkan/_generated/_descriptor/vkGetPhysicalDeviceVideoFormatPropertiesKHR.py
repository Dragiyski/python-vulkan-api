from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceVideoFormatPropertiesKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pVideoFormatInfo', 'pVideoFormatPropertyCount', 'pVideoFormatProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pVideoFormatInfo': {
        'type': CPointerType(CComplexType('VkPhysicalDeviceVideoFormatInfoKHR')),
        'is_string': False,
        'output': False,
    },
    'pVideoFormatPropertyCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pVideoFormatProperties': {
        'type': CPointerType(CComplexType('VkVideoFormatPropertiesKHR')),
        'is_string': False,
        'length': [['pVideoFormatPropertyCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_VIDEO_PROFILE_FORMAT_NOT_SUPPORTED_KHR', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_VIDEO_PROFILE_OPERATION_NOT_SUPPORTED_KHR', 'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_IMAGE_USAGE_NOT_SUPPORTED_KHR', 'VK_ERROR_VIDEO_PICTURE_LAYOUT_NOT_SUPPORTED_KHR', 'VK_ERROR_VIDEO_PROFILE_CODEC_NOT_SUPPORTED_KHR'}
