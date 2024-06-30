from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceExternalImageFormatPropertiesNV'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'format', 'type', 'tiling', 'usage', 'flags', 'externalHandleType', 'pExternalImageFormatProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'tiling': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'externalHandleType': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pExternalImageFormatProperties': {
        'type': CPointerType(CComplexType('VkExternalImageFormatPropertiesNV')),
        'is_string': False,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_OUT_OF_DEVICE_MEMORY', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_FORMAT_NOT_SUPPORTED'}
