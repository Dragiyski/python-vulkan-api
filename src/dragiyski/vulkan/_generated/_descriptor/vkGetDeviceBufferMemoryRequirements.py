from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetDeviceBufferMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'pInfo', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pInfo': {
        'type': CPointerType(CComplexType('VkDeviceBufferMemoryRequirements')),
        'is_string': False,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkMemoryRequirements2')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
