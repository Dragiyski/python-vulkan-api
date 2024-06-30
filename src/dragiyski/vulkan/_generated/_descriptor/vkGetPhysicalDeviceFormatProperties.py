from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetPhysicalDeviceFormatProperties'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'format', 'pFormatProperties']
_argument_info_ = {
    'physicalDevice': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'format': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
    'pFormatProperties': {
        'type': CPointerType(CComplexType('VkFormatProperties')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
