from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetBufferMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'buffer', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'buffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkMemoryRequirements')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
