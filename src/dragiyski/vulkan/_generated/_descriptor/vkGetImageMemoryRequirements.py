from ..._ctypes import *

_category_ = 'function'
_name_ = 'vkGetImageMemoryRequirements'
_constructor_ = 'VKAPI_CALL'
_argument_list_ = ['device', 'image', 'pMemoryRequirements']
_argument_info_ = {
    'device': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pMemoryRequirements': {
        'type': CPointerType(CComplexType('VkMemoryRequirements')),
        'is_string': False,
    },
}
_return_type_ = CVoidType()
