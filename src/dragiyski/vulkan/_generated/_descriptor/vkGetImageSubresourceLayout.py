from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetImageSubresourceLayout'
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
        'type': CPointerType(CComplexType('VkImageSubresource')),
        'is_string': False,
    },
    'pLayout': {
        'type': CPointerType(CComplexType('VkSubresourceLayout')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
