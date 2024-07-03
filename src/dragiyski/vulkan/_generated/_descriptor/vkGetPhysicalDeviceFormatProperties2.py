from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetPhysicalDeviceFormatProperties2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['physicalDevice', 'format', 'pFormatProperties']
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
    'pFormatProperties': {
        'type': CPointerType(CComplexType('VkFormatProperties2')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
