from ..._ctypes import *

_category_ = 'procedure'
_name_ = 'vkGetDeviceQueue2'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pQueueInfo', 'pQueue']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
        'output': False,
    },
    'pQueueInfo': {
        'type': CPointerType(CComplexType('VkDeviceQueueInfo2')),
        'is_string': False,
        'output': False,
    },
    'pQueue': {
        'type': CPointerType(CIntType('c_void_p')),
        'is_string': False,
        'output': True,
    },
}
_return_type_ = CVoidType()
