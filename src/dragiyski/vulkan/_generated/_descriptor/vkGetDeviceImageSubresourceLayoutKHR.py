from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDeviceImageSubresourceLayoutKHR'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pInfo', 'pLayout']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkDeviceImageSubresourceInfoKHR')),
        'is_string': False,
    },
    'pLayout': {
        'type': CPointerType(CComplexType('VkSubresourceLayout2KHR')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
