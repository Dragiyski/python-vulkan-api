from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceImageFormatProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'format', 'type', 'tiling', 'usage', 'flags', 'pImageFormatProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'tiling': {
        'type': CIntType('c_int'),
        'is_string': False,
        'output': False,
    },
    'usage': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'is_string': False,
        'output': False,
    },
    'pImageFormatProperties': {
        'type': CPointerType(CComplexType('VkImageFormatProperties')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CIntType('c_int')
_success_code_list_ = {'VK_SUCCESS'}
_error_code_list_ = {'VK_ERROR_FORMAT_NOT_SUPPORTED', 'VK_ERROR_OUT_OF_HOST_MEMORY', 'VK_ERROR_OUT_OF_DEVICE_MEMORY'}
