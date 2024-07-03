from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetImageSubresourceLayout'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'pSubresource', 'pLayout']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pSubresource': {
        'type': CPointerType(CComplexType('VkImageSubresource')),
        'is_string': False,
        'output': False,
    },
    'pLayout': {
        'type': CPointerType(CComplexType('VkSubresourceLayout')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
