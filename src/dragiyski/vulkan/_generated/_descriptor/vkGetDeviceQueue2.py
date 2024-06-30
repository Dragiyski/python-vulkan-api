from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDeviceQueue2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pQueueInfo', 'pQueue']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pQueueInfo': {
        'type': CPointerType(CComplexType('VkDeviceQueueInfo2')),
        'is_string': False,
    },
    'pQueue': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
