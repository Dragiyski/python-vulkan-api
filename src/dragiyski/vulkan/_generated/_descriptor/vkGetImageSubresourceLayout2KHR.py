from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetImageSubresourceLayout2KHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'pSubresource', 'pLayout']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pSubresource': {
        'type': CPointerType(CComplexType('VkImageSubresource2KHR')),
        'is_string': False,
    },
    'pLayout': {
        'type': CPointerType(CComplexType('VkSubresourceLayout2KHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
