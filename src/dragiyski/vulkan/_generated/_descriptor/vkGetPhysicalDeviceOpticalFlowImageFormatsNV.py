from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceOpticalFlowImageFormatsNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'pOpticalFlowImageFormatInfo', 'pFormatCount', 'pImageFormatProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pOpticalFlowImageFormatInfo': {
        'type': CPointerType(CComplexType('VkOpticalFlowImageFormatInfoNV')),
        'is_string': False,
        'output': False,
    },
    'pFormatCount': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
        'output': True,
    },
    'pImageFormatProperties': {
        'type': CPointerType(CComplexType('VkOpticalFlowImageFormatPropertiesNV')),
        'is_string': False,
        'length': [['pFormatCount']],
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS', 'VK_INCOMPLETE'}
_error_code_list_ = {'VK_ERROR_FORMAT_NOT_SUPPORTED', 'VK_ERROR_INITIALIZATION_FAILED', 'VK_ERROR_EXTENSION_NOT_PRESENT'}
